from datetime import datetime
from bisect import bisect_left
import argparse
import xml.etree.ElementTree as ElemTree

from .settings_ekahau import TX_POWER_TABLE

def power_level_lookup(model, channel, dbm):
    """
    Helper function: Convert a dBm Tx power level to a Cisco power level
    (1-8, where 1 is strongest and 8 is weakest). If the exact dBm lookup fails
    the closest approximation will be used.

    Args:
        channel (int): 2.4/5Ghz channel number.
        dbm (int): dBm power level.

    Returns:
        int: Cisco power level from 1 to 8, or 0 if dbm is zero
        (radio is disabled).

    Raises:
        ValueError: Caused from invalid channel and dbm information.
    """
    channel, dbm = int(channel), int(dbm) # type coercions
    if dbm == 0:
        return 0 # disabled

    power_model = [tk for tk in TX_POWER_TABLE.keys()
            if model in tk or tk in model]
    if not power_model:
        raise ValueError("dBm to Cisco power table not found")
    elif len(power_model) > 2:
        raise ValueError("Multiple power levels found")

    power_model = power_model[0]
    power_table = TX_POWER_TABLE[power_model]
    if isinstance(power_table, str):
        # may be a reference to another table, load that instead
        power_table = TX_POWER_TABLE[power_table]
    if channel not in power_table.keys():
        raise ValueError("Unsupported channel " + str(channel))

    if power_table[channel].get(dbm):
        return power_table[channel][dbm]
    else:
        # exact dBm not found, find the closest power level
        dbmlist = sorted(power_table[channel].keys())
        index = bisect_left(dbmlist, dbm)
        if index == 0:
            return power_table[channel][dbmlist[0]] # first item
        elif index == len(dbmlist):
            return power_table[channel][dbmlist[-1]] # last item
        else:
            # get closest power level, prefer smaller
            if dbmlist[index] - dbm < dbm - dbmlist[index - 1]:
                return power_table[channel][dbmlist[index]]
            else:
                return power_table[channel][dbmlist[index - 1]]

def generate_commands(name, apmodel, freq_type, chan, power, monitormode=False):
    """
    Generate Cisco WLC CLI commands for the given AP data.

    Args:
        name (str): AP name.
        apmodel (str): AP model.
        freq_type (str): Frequency type as an 802.11 type (a/n, b/g/n, etc.)
        chan (int): Radio channel
        power (int): Radio Power as dBm.
        monitormode (bool): Optional - If True, set APs with transmit power 0 to
            monitor mode instead of disabling them.

    Returns:
        str: A list of command strings.
    """
    commands = []
    if 'a/n' in str(freq_type) or freq_type == 5:
        freq_type = 'a' # a is the 5Ghz radio
    elif (apmodel.upper() == 'AP3800I'
            or apmodel.upper() == 'AP3802I'
            or apmodel.upper() == 'AP2802I'):
        # special case for 3800s, 2.4Ghz radio only
        freq_type = '-abgn' # abgn is dual 2.4/5Ghz for the 3800s
    elif 'b/g/n' in str(freq_type) or freq_type == 2:
        freq_type = 'b' # b is the 2.4Ghz radio

    # convert dBm to Cisco power levels
    power = power_level_lookup(apmodel, chan, power)

    prefix = 'config 802.11' + freq_type
    disable_command = prefix + ' disable ' + name
    # for 1815w APs, which have 2 "2.4Ghz" radios - one 802.11n and
    # a BLE radio. We need to ignore the second 2.4Ghz radio for now
    if disable_command in commands and freq_type == 'b':
        return

    # save WLC config commands
    commands.append(disable_command)
    if power == 0:
        if monitormode and (apmodel.upper() == 'AP3802I'
                or apmodel.upper() == 'AP2802I'): # set to monitor mode
            commands.append(prefix + ' role ' + name +
                    ' manual monitor')
    else:
        if apmodel.upper() == 'AP3802I' or apmodel.upper() == 'AP2802I':
            commands.append(prefix + ' role ' + name +
                    ' manual client-serving')
        commands.append(prefix + ' txpower ap ' + name + ' ' +
                str(power))
        commands.append(prefix + ' channel ap ' + name + ' ' +
                str(chan))
        if freq_type == 'a': # add channel width for 5Ghz radios
            commands.append(prefix + ' chan_width ' + name + ' 20')
        commands.append(prefix + ' enable ' + name)
    return commands

def ekahau_to_WLC(xml_data, comments=True, monitormode=False):
    """
    Convert an Ekahau site survey/project XML file to Cisco WLC
    configuration commands. This pulls AP name, channel info, transmit
    power, and enable/disable status and returns a configuration file.

    Args:
        xml_data (str): XML data as a string.
        comments (bool): Optional - If True, include comments in the result
            (prepended with #)
        monitormode (bool): Optional - If True, set APs with transmit power 0 to
            monitor mode instead of disabling them.

    Returns:
        str: A 2-tuple of a filename and a string with newlines containing
        configuration commands.
    """
    ns = {'cisco': "http://importexport.cisco.com/1.0"}
    # load up project XML structure
    ek_root = ElemTree.fromstring(xml_data)
    ek_site = ek_root.find('./cisco:Maps/cisco:Site', ns)
    site_name = ek_site.attrib['name'] # get site name for autogen filename
    ek_floors = ek_root.findall( # xpath for floor tags
            './cisco:Maps/cisco:Site/cisco:Building/cisco:Floor', ns)

    if comments:
        commands = ["##### WLC Config for " + site_name + ", generated at " +
                str(datetime.now()) + " #####"]
    else:
        commands = []
    # iterate over each floor in the project building
    for floor in ek_floors:
        floor_name = floor.attrib['name']
        if comments: # save floor name
            commands.append("#### Floor " + floor_name + " ####")

        # iterate over each AP
        for ap in floor.findall('cisco:PlannedAp', ns):
            name = ap.attrib['name']
            apmodel = ap.attrib['apModel']
            if comments:
                commands.append("### " + name + " (" + apmodel + ") ###")
            for radio in ap.findall('cisco:Radio', ns):
                freq_type = radio.attrib['ifType']
                power = radio.attrib['txPowerLevel']
                chan = radio.find('ChannelDefinition').attrib['channelNumber']

                radio_cmds = generate_commands(name, apmodel, freq_type,
                        chan, power, monitormode=monitormode)
                if not radio_cmds:
                    continue
                commands.extend(radio_cmds)
                commands.append('') # newline

    filename = site_name + '-config.txt'
    return filename, '\n'.join(commands)

if __name__ == '__main__':
    # read arguments if this was run as a script
    optparser = argparse.ArgumentParser()
    optparser.add_argument('projectfile', metavar='projectfile', type=str,
            help='Ekahau project XML file')
    optparser.add_argument('-o', '--outfile', metavar='outfile', type=str,
            help='Output config filename, overrides name taken from project')
    optparser.add_argument('-d', '--disable-comments', action='store_false',
            help='Disable comments in config file')
    optparser.add_argument('-m', '--monitor', action='store_true',
            help='Use monitor mode instead of disabling APs')
    optparser.add_argument('-p', '--print', action='store_true',
            help='Print output config instead of writing to a file')
    args = optparser.parse_args()
    args = vars(args)

    with open(args['projectfile']) as inf:
        xmldata = inf.read()
    result = ekahau_to_WLC(xmldata, comments=args['disable_comments'],
            monitormode=args['monitor'])
    if args['print']:
        print(result[1])
    else:
        filename = (args['outfile'] if args['outfile'] else result[0])
        with open(filename, 'w') as outf:
            outf.write(result[1])
