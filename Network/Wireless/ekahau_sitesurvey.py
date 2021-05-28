import io, traceback, json
from zipfile import ZipFile
from collections import namedtuple
from .ekahau_conversion import generate_commands

AP = namedtuple('AP', ['name', 'model', 'radios', 'notes'])
RadioData = namedtuple('RadioData', ['type', 'antennatype', 'channel', 'power',
        'enabled'])

class EkahauSiteSurvey(object):
    """
    Manage and apply Ekahau Site Survey project files (.esx) to Cisco WLC
    controllers.
    """
    def __init__(self):
        pass

    def get_ap_data_from_esx(self, filedata=None, filename=None):
        """
        Read AP name and radio data from an ESX site survey file, passed as
        either raw bytes or from a filename.

        Args:
            filedata (str): Optional - File data stream.
            filename (str): Optional - File name as a string.

        Returns:
            (AP): A list of AP namedtuples.
        
        Raises:
            Value Error: Caused if JSON data is formatted incorrectly or is 
                missing data.
        """
        # Contains a tuples (errored item, message)
        errors = []

        if not filedata and not filename:
            raise ValueError("filedata or filename must be specified")
        with (ZipFile(filename, 'r') if filename else
                ZipFile(io.BytesIO(filedata))) as esxfile:
            if ('simulatedRadios.json' not in esxfile.namelist()
                    or 'accessPoints.json' not in esxfile.namelist()
                    or 'antennaTypes.json' not in esxfile.namelist()):
                raise ValueError("AP data not found in project file")
            self.ap_names = {}
            apnames = {} # key is AP ID and value is AP name, note ID
            with esxfile.open('accessPoints.json') as apfile:
                js = json.loads(apfile.read())
                if not js.get('accessPoints'):
                    raise ValueError("Incorrectly formatted AP JSON data")
                for ap in js['accessPoints']:
                    if 'id' not in ap.keys() or 'name' not in ap.keys():
                        continue # skip this AP
                    noteid = (ap['noteIds'][0] if ap.get('noteIds') else None)
                    apnames[ap['id']] = (ap['name'], noteid)
            self.ap_names = apnames.copy()

            antennatypes = {} # key is antenna type ID and value is AP model
            with esxfile.open('antennaTypes.json') as antennafile:
                js = json.loads(antennafile.read())
                if not js.get('antennaTypes'):
                    raise ValueError("Incorrectly formatted antenna JSON data")
                for antenna in js['antennaTypes']:
                    if "BLUETOOTH" in antenna['radioTechnology']:
                        continue # skip bluetooth radios
                    if 'apModel' in antenna.keys():
                        antennatypes[antenna['id']] = antenna['apModel']
                    else:
                        # Documenting error
                        error = (antenna['name'],
                                'anntenna does not have associated ap model')
                        errors.append(error)

            radiodata = {} # key is AP ID and value is a list of RadioDatas
            with esxfile.open('simulatedRadios.json') as radiofile:
                js = json.loads(radiofile.read())
                if not js.get('simulatedRadios'):
                    raise ValueError("Incorrectly formatted radio JSON data")
                for radio in js['simulatedRadios']:
                    if "BLUETOOTH" in radio['radioTechnology']:
                        continue # skip bluetooth radios
                    channeltype = (5 if radio['channel'][0] > 14 else 2)

                    rd = RadioData(channeltype, radio['antennaTypeId'],
                            radio['channel'][0], radio.get('transmitPower', 0),
                            radio['enabled'])
                    if radiodata.get(radio['accessPointId']):
                        radiodata[radio['accessPointId']].append(rd)
                    else:
                        radiodata[radio['accessPointId']] = [rd]

            notes = {}
            if 'notes.json' in esxfile.namelist():
                with esxfile.open('notes.json') as notesfile:
                    js = json.loads(notesfile.read())
                    if not js.get('notes'):
                        raise ValueError("Incorrectly formatted notes data")
                    for note in js['notes']:
                        notes[note['id']] = note['text']

            aplist = []
            for apid in apnames.keys():
                # we shouldn't get a disagree on AP model for its radios
                apmodels = []
                if apid in radiodata.keys():
                    for rd in radiodata[apid]:
                        apmodels.append(antennatypes[rd.antennatype])
                else:
                    # Documenting error - No radios found for AP ID
                    errors.append((apnames[apid][0], 
                            "No radio information provided"))
                    continue
                    
                if len(set(apmodels)) > 1:
                    raise ValueError("AP radios match different models: " +
                            ', '.join(apmodels))
                apmodel = list(set(apmodels))[0]
                if notes.get(apnames[apid][1]):
                    import logging
                    logging.info(notes[apnames[apid][1]])
                aplist.append(AP(apnames[apid][0], apmodel, radiodata[apid],
                        notes.get(apnames[apid][1])))

            return aplist, errors

    def validate_ap_list(self, apdatalist):
        """
        Validate the list of APs for power, channel settings, etc.

        Args:
            apdatalist (list): A list of AP namedtuples.

        Returns:
            None or list: None if this is valid; Otherwise a list of tuples 
            containing the AP name, model, and error message.

        Raises:
            ValueError: Caused if radio information from APs is invalid.
        """
        errors = []
        for ap in apdatalist:
            for radio in ap.radios:
                try:
                    if not ((1 <= radio.channel <= 13 or (radio.channel % 2 == 0
                            and (36 <= radio.channel <= 64
                            or 100 <= radio.channel <= 144))
                            or (radio.channel % 2 == 1 and
                            149 <= radio.channel <= 165)
                            ) and radio.channel not in [130, 163]):
                        raise ValueError("Invalid channel " +str(radio.channel))
                    if radio.power > 30:
                        raise ValueError("Power set too high (" +
                                str(radio.power) + "dBm)")
                    if radio.type == 5 and 1 <= radio.channel <= 13:
                        raise ValueError("2.4Ghz channel set for 5Ghz radio")
                    # don't check for 5Ghz channel on 2.4Ghz radio since some
                    # APs support that kind of thing (like Cisco 3800s)
                    generate_commands(ap.name, ap.model, radio.type,
                            radio.channel, radio.power)
                except Exception as e:
                    errors.append((ap.name, ap.model, str(e)))
        return (errors if errors else None)

    def generate_wlc_commands(self, apdatalist, comments=False):
        """
        Generate Cisco WLC CLI commands from a list of AP namedtuples.

        Args:
            apdatalist (list): A list of AP namedtuples.
            comments (bool): Optional - If True, include additional comments.
        Returns:
            list: A list of command strings.
        """
        commands = []
        apdatalist.sort()
        for ap in apdatalist:
            if comments:
                commands.append("### " + ap.name + " (" + ap.model + ") ###")
            for radio in ap.radios:
                if (not radio.enabled and ap.notes
                        and 'disable' in ap.notes.lower()):
                    # disabled AND notes say this AP is disabled: turn off
                    rcmd = generate_commands(ap.name, ap.model, radio.type,
                            radio.channel, 0, monitormode=False)
                else:
                    # set to monitor mode by default
                    rcmd = generate_commands(ap.name, ap.model, radio.type,
                            radio.channel, radio.power, monitormode=True)

                if not rcmd:
                    continue # skipped radio
                commands.extend(rcmd)
                commands.append('')

        return commands
