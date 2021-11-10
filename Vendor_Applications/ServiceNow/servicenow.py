from builtins import next
from builtins import str
from builtins import object
import requests, logging, json
from . import settings
from datetime import datetime, timedelta

class ServiceNowAPIError(Exception):
    """
    A ServiceNowAPIError occurs when we receive anything but a 200 response
    from Service Now.
    """
    pass

class ServiceNow(object):
    """
    An abstraction layer for working with the service now REST API.
    Args:
        user (str): Username required for making the API calls.
        pwd (str): Password required for making the API calls.
        url (str): The URL may be the production or development version of
                ServiceNow.
    """
    _headers = {"Content-Type":"application/json", "Accept":"application/json"}

    def __init__(self, user, pwd, url):
        self._user = user
        self._pwd = pwd
        self._url = url

    def get_dev_info(self):
        """
        Specify development status; this is read by TOAST.

        Returns:
            str: The development status
        """
        return "Production"

    def get_assignmentgroup_sysid(self, name):
        """
        Convert a uNID to a user sys_id.

        Args:
            unid (str): uNID to convert to a sys_id.

        Returns:
            str: sys_id of the user.
        """
        url = (self._url + f'/api/now/table/sys_user_group?sysparm_query=name={name}')
        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        response.json()['error']['detail'])
            except:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + ', text:' + response.text)

        data = response.json()
        if data['result'] == None:
            raise ValueError (f"Could not find Service now Sys_ID for {name}")
        return data['result'][0]['sys_id']

    def get_unid_sysid(self, unid):
        """
        Convert a uNID to a user sys_id.

        Args:
            unid (str): uNID to convert to a sys_id.

        Returns:
            str: sys_id of the user.
        """
        url = (self._url + '/api/now/table/sys_user?sysparm_limit=1&user_name='+
                str(unid))

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        response.json()['error']['detail'])
            except:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + ', text:' + response.text)

        data = response.json()
        if data['result'] == None:
            raise ValueError (f"Could not find Service now Sys_ID for {unid}")
        return data['result'][0]['sys_id']

    def get_sysid_user(self, sys_id):
        """
        Returns a user name for a given sys_id.

        Args:
            sys_id (str): sys_id of the user.

        Returns:
            str: First and last name of the user.

        Raises:
            Exception: If the request fails.
        """
        if not sys_id:
            return sys_id

        url = (self._url + "/api/now/table/sys_user?sysparm_query=" +
                "sys_idCONTAINS" + sys_id)
        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))

        return response.json()["result"][0]["name"]

    def get_stdchng_templates(self):
        """
        Create a standard change.

        Args:
            sys_id (str): The sys_id for the standard change template for the
                record producer to use.

        Returns:
            str: sys_id for the created change.

        Raises:
            ServiceNowAPIError: If an error occured when creating a standard
            change.
        """
        url = (self._url + '/api/sn_chg_rest/change/standard/template')

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        str(response.json()['error']['detail']))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')
            except ValueError:
                logging.error('Service Now response code ' +
                        str(response.status_code) + ': ' + str(response.text))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')

        data = response.json()
        return data['result']

    def _get_stdchng(self,ticketnumber):
        """
        get sysid for standard change by ticket number

        Args:
            sys_id (str): The sys_id for the standard change template for the
                record producer to use.

        Returns:
            str: sys_id for the created change.

        Raises:
            ServiceNowAPIError: If an error occured when creating a standard
            change.
        """
        url = (self._url + f'/api/sn_chg_rest/v1/change/standard?sysparm_query=number={ticketnumber}')

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        str(response.json()['error']['detail']))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')
            except ValueError:
                logging.error('Service Now response code ' +
                        str(response.status_code) + ': ' + str(response.text))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')

        data = response.json()
        return data['result'][0]

    def make_switch_code_stdchng(self,hostnames,startdate,enddate,assignee):
        """
        Create a standard change.

        Args:
            sys_id (str): The sys_id for the standard change template for the
                record producer to use.

        Returns:
            str: sys_id for the created change.

        Raises:
            ServiceNowAPIError: If an error occured when creating a standard
            change.
        """
        sys_id = '036320db1378a60452aa31f18144b000'
        url = (f'{self._url}/api/sn_chg_rest/change/standard/{sys_id}')

        response = requests.post(url, auth=(self._user, self._pwd),
                headers=self._headers, data=json.dumps({'start_date': str(startdate),
                'end_date': (str(enddate)),
                'justification': "Software is losing Support. " 
                                 "Code may need to be modified to accommodate a feature or security issue on the switch.",
                'assignment_group': str(self.get_assignmentgroup_sysid('UIT - NCI - Network Edge Services (NEEI)')) ,
                'requested_by': str(self.get_unid_sysid('u0800148')),
                'opened_by': str(self.get_unid_sysid('u0800148')),
                'description':f'Upgrade/Downgrade code on the following: \r\n{hostnames}',
                'assigned_to': str(self.get_unid_sysid(assignee))}))

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        str(response.json()['error']['detail']))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')
            except ValueError:
                logging.error('Service Now response code ' +
                        str(response.status_code) + ': ' + str(response.text))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')

        data = response.json()
        return data['result']

    def make_switch_install_stdchng(self,hostname):
        """
        Create a standard change.

        Args:
            sys_id (str): The sys_id for the standard change template for the
                record producer to use.

        Returns:
            str: sys_id for the created change.

        Raises:
            ServiceNowAPIError: If an error occured when creating a standard
            change.
        """
        sys_id = '033e763213f0e604ae6d53228144b0e4'
        url = (f'{self._url}/api/sn_chg_rest/change/standard/{sys_id}')

        response = requests.post(url, auth=(self._user, self._pwd),
                headers=self._headers, data=json.dumps({'start_date': str(datetime.now()),
                'end_date': (str(datetime.now()+timedelta(hours=5))),
                'justification': "Hardware is losing support. Replacing to keep pace with Innovation",
                'work_notes_list': f'replacing: {hostname}',
                'assigned_to': str(self.get_unid_sysid('u0800148'))}))

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        str(response.json()['error']['detail']))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')
            except ValueError:
                logging.error('Service Now response code ' +
                        str(response.status_code) + ': ' + str(response.text))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')

        data = response.json()
        return data['result']

    def create_stdchng(self, sys_id):
        """
        Create a standard change.

        Args:
            sys_id (str): The sys_id for the standard change template for the
                record producer to use.

        Returns:
            str: sys_id for the created change.

        Raises:
            ServiceNowAPIError: If an error occured when creating a standard
            change.
        """
        url = (self._url + '/api/sn_sc/servicecatalog/items/'+ str(sys_id) +
                '/submit_producer')

        response = requests.post(url, auth=(self._user, self._pwd),
                headers=self._headers, data="{}")

        if response.status_code != 200:
            try:
                logging.error('Service Now response code: ' +
                        str(response.status_code) + '. Error Details: ' +
                        str(response.json()['error']['detail']))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')
            except ValueError:
                logging.error('Service Now response code ' +
                        str(response.status_code) + ': ' + str(response.text))
                raise ServiceNowAPIError('Error creating/updating/closing ' +
                        'Standard Change')

        data = response.json()
        logging.info('Created standard change : ' + data['result']['number'])
        return data['result']['sys_id']

    def assign_stdchng(self, sys_id, unid):
        """
        Assign a user to the standard change and add planned start/stop times.

        Args:
            sys_id (str): The change sys_id.
            unid (str): The uNID of the user to assign to the change.

        Raises:
            ServiceNowAPIError: If an error occured when updating a standard
            change.
        """
        now = datetime.now()
        url = (self._url + '/api/now/table/change_request/' + str(sys_id))

        response = requests.put(url, auth=(self._user, self._pwd),
                headers=self._headers, data=json.dumps({'start_date': str(now),
                'end_date': (str(now + timedelta(hours=1))),
                'assigned_to': str(self.get_unid_sysid(unid))}))

        if response.status_code != 200:
            logging.error('Service Now response code: ' +
                    str(response.status_code) + '. Error Details: ' +
                    response.json()['error']['detail'])
            raise ServiceNowAPIError('Error creating/updating/closing ' +
                    'Standard Change')

    def change_stdchng_state(self, sys_id, state):
        """
        Change the state of the standard change.

        Args:
            sys_id (str): The change sys_id.
            state (int): State code.

        Raises:
            ServiceNowAPIError: If an error occured when updating a standard
            change.
        """
        url = (self._url + '/api/now/table/change_request/' + sys_id)

        response = requests.put(url, auth=(self._user, self._pwd),
                                headers=self._headers, data=json.dumps({'state':
                str(settings.ChangeStates[state].value)}))

        if response.status_code != 200:
            logging.error('Service Now response code: ' +
                    str(response.status_code) + '. Error Details: ' +
                    response.json()['error']['detail'])
            raise ServiceNowAPIError('Error creating/updating/closing ' +
                    'Standard Change')


    def close_stdchng(self, sys_id, close_code, close_notes):
        """
        Close a standard change.

        Args:
            sys_id (str): The change sys_id.
            close_code (str): 'Successful', 'Successful with issues' or
                'Unsuccessful'.
            close_notes (str): 4000 Character limit of close notes.

        Raises:
            ServiceNowAPIError: If an error occured when closing a standard
            change.
        """
        url = (self._url + '/api/now/table/change_request/' + sys_id)

        response = requests.put(url, auth=(self._user, self._pwd),
                headers=self._headers, data=json.dumps({'state': '3',
                'close_code': str(close_code), 'close_notes':str(close_notes)}))

        if response.status_code != 200:
            logging.error('Service Now response code: ' +
                    str(response.status_code) + '. Error Details: ' +
                    response.json()['error']['detail'])
            raise ServiceNowAPIError('Error creating/updating/closing ' +
                    'Standard Change')

    def fw_stdchng(self):
        """
        Create a weekly firewall push standard change.

        Returns:
            str: sys_id of the created change.
        """
        return self.create_stdchng(settings.fw_stdchng_sysid)

    def new_vlan_stdchng(self):
        """
        Create a new VLAN/SVI standard change.

        Returns:
            str: sys_id of the created change.
        """
        return self.create_stdchng(settings.new_vlan_sysid)

    def get_open_tickets(self, short_description):
        """
        Returns a list of task numbers matching the short description of the
        ticket.

        Args:
            short_description (str): The short despscription of the task item.

        Returns:
            list: ServiceNow TASK numbers.
        """
        url = (self._url + "/api/now/table/sc_task?sysparm_query=" +
                "short_description CONTAINS" +
                short_description.replace(" ", "%20") + "&active=true")

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))

        ticket_information = response.json()
        task_numbers = [task['number'] for task in ticket_information['result']]
        return task_numbers

    def check_ticket(self, number):
        """
        Check if ticket is valid and open on service now

        Args:
            number (str): the ticket numer to check

        Returns:
            bool: True if valid, else false
        """
        if "TASK" in number.upper():
            url = (self._url + "/api/now/table/sc_task?sysparm_query=" +
                    f"number={number}^active=true")
        elif "INC" in number.upper():
            url = (f"{self._url}/api/now/table/incident?sysparm_query=" +
                    f"number={number}^active=true")
        elif "RITM" in number.upper():
            url = (f"{self._url}/api/now/table/sc_req_item?sysparm_query=" +
                    f"number={number}^active=true")
        else:
            raise ValueError("Only TASKs, RITMs and INCs are supported!")

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))

        ticket_information = response.json()

        tasks = [task['number'] for task in ticket_information['result']]
        return True if tasks else False

    def _get_task_info(self, task_number):
        """
        Collects more information to be added to the dict created in
        get_ticket_info.

        Args:
            task_number (str): A ServiceNow TASK number.

        Returns:
            dict: Additional ticket information.
        """
        url = (self._url + "/api/now/table/sc_task?sysparm_query=" +
                "numberCONTAINS" + task_number)
        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))
        response = response.json()["result"][0]

        return {
                "number": task_number,
                "short_description": response["short_description"],
                "created_on": response["sys_created_on"],
                "sys_id": response["sys_id"],
                "ritm_sys_id": response['request_item']['value'],
        }

    def get_incident_info(self, incident_number):
        """
        Gets related information about an incident.

        Args:
            incident_number (str): A ServiceNow INC number.

        Returns:
            dict: Additional ticket information.

        Raises:
            Exception: Caused if issue with API call.
        """
        url = (f"{self._url}/api/now/table/incident?sysparm_query=" +
                f"number={incident_number}")
        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))
        response = response.json()["result"][0]

        return {
                "number": incident_number,
                "short_description": response["short_description"],
                "created_on": response["sys_created_on"],
                "sys_id": response["sys_id"],
        }

    def get_ticket_info(self, task_number):
        """
        Return the contents of a ticket.

        Args:
            task_number (str): A ServiceNow TASK number.

        Returns:
            dict: Data within ticket fields.
        """
        fields = self._get_task_info(task_number)

        # Get extra TASK attributes
        url = (self._url + "/api/now/table/sc_item_option_mtom?sysparm_query=" +
                "request_itemCONTAINS" + fields['ritm_sys_id'] +
                "&sysparm_fields=sc_item_option.value%2C" +
                "sc_item_option.item_option_new.name")

        response = requests.get(url, auth=(self._user, self._pwd),
                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))

        response = response.json()["result"]

        # Get requested user
        try:
            fields['requested_by'] = self.get_sysid_user(
                    next(field["sc_item_option.value"] for field in response if
                    field["sc_item_option.item_option_new.name"] =="requester"))
        except StopIteration:
            fields['requested_by'] = '' # unknown user?

        # Additional fields
        for entry in response:
            field_name = entry["sc_item_option.item_option_new.name"].split("_")
            field_name = field_name[len(field_name) - 1]
            field_value = entry["sc_item_option.value"]
            fields[field_name] = field_value

        return fields

    def close_task(self, sys_id, unid, worknotes=None):
        """
        Updates the task to a close state. Changes the task state to be
        "closed complete". The user accredited to closing the ticket is the user
        provided by the unid. Closing the ticket with a closing work note is
        recommended.

        Args:
            sys_id (str): tas_id of the ticket.
            unid (str): The user's unid.
            worknotes (str): Optional - A closing work note.

        Raises:
            Exception: Failed response.
        """
        url = self._url + '/api/now/table/sc_task/' + sys_id

        fields = {"state": "3", "assigned_to": unid}
        if worknotes is not None:
            fields.update({"work_notes": worknotes})
        response = requests.put(url, auth=(self._user, self._pwd),
                headers=self._headers, data=json.dumps(fields))

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)+
                    ": " + str(response.text))

    def get_user_name(self, unid):
        """
        Returns a user's first and last name identified by a uNID.

        Args:
            unid (str): A unid has the form uXXXXXXX, where an X represents a
                digit.

        Returns:
            str: A space-seperated first and last name.

        Raises:
            Exception: Failed response.
        """
        unid = "0" + unid[1:len(unid)]
        url = self._url + "/api/now/table/sys_user?u_employee_id=" + unid

        response = requests.get(url, auth=(self._user, self._pwd),
                                headers=self._headers)

        if response.status_code != 200:
            raise Exception("Request failed, code " + str(response.status_code)
                            + ": " + str(response.text))

        return response.json()["result"][0]["name"]

    def add_txt_attachment(self, ticket_number, data, file_name):
        """
        Attaches a text file to a given ticket in service now.

        Args:
            ticket_number (str): I.E. TASK1234567 or INC1234567.
            data (bytes): Raw bytes of string information for txt.
            file_name (str): Name of txt file to attach.

        Raises:
            ValueError: Caused if ticket number is not a task or inc.
            Exception: Caused by error in request.
        """
        if "task" in ticket_number.lower():
            ticket_type = "task"
            sys_id = self._get_task_info(ticket_number)["sys_id"]
        elif "inc" in ticket_number.lower():
            ticket_type = "incident"
            sys_id = self.get_incident_info(ticket_number)["sys_id"]
        else:
            raise ValueError("Only supports TASKs and INCs.")
        url = f"{self._url}/api/now/attachment/file"
        args = {
            "table_name": ticket_type,
            "table_sys_id": sys_id,
            "file_name": f"{file_name}.txt"
        }
        header = {
            "Content-Type": "text/plain",
            "Accept": "application/json"
        }
        response = requests.post(url, params=args, headers=header, data=data,
                auth=(self._user, self._pwd))
        if response.status_code != 201:
            raise Exception(f"Request failed, code {response.status_code}: " +
                    f"{response.text}")

    def remove_txt_attachment(self, ticket_number, file_name):
        """
        Removes an attached text file from a given ticket in service now.

        Args:
            ticket_number (str): I.E. TASK1234567 or INC1234567.
            file_name (str): Name of attached file.

        Raises:
            ValueError: Caused if ticket number is not a task or inc.
            Exception: Caused by error in request.
        """
        if "task" in ticket_number.lower():
            ticket_type = "task"
            sys_id = self._get_task_info(ticket_number)["sys_id"]
        elif "inc" in ticket_number.lower():
            ticket_type = "incident"
            sys_id = self.get_incident_info(ticket_number)["sys_id"]
        else:
            raise ValueError("Only supports TASKs and INCs.")
        url = f"{self._url}/api/now/attachment"
        args = {
            "sysparm_query": f"table_sys_id={sys_id}",
        }
        response = requests.get(url, params=args, headers=self._headers,
                auth=(self._user, self._pwd))
        if response.status_code != 200:
            raise Exception(f"Request failed, code {response.status_code}: " +
                    f"{response.text}")
        file_sys_id = None
        for file_attachment in response.json()["result"]:
            if file_attachment["file_name"] == file_name:
                file_sys_id = file_attachment["sys_id"]
        if not file_sys_id:
            raise Exception(f"File: {file_name} cannot be found.")
        url = f"{self._url}/api/now/attachment/{file_sys_id}"
        response = requests.delete(url, headers=self._headers,
                auth=(self._user, self._pwd))
        if response.status_code != 204:
            raise Exception(f"Request failed, code {response.status_code}: " +
                    f"{response.text}")