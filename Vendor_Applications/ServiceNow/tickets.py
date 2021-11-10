from __future__ import absolute_import
from builtins import object
from . import helpers


class TicketRunner(object):
    """
    Superclass that defines common ticket/module functions such as validate()
    and run().
    """
    def __init__(self):
        pass

    def validate(self):
        """
        Validate function. This should accept information from the ServiceNow
        ticket, and return None or a converted object (optional) if validated or
        raise an Exception if validation failed.
        """
        raise NotImplementedError()

    def run(self):
        """
        Run/ticket completion function. This should accept information from
        the ServiceNow ticket, and return a string with a status message if
        successful or raise an Exception if completing the ticket failed.
        """
        raise NotImplementedError()

class InfobloxRecords(TicketRunner):
    """
    Handle tickets that change Infoblox records.

    Args:
        ib_obj (Infoblox): InfobloxTools instance.
    """
    def __init__(self, ib_obj):
        TicketRunner.__init__(self)
        self.infoblox = ib_obj

    def validate(self, ticket):
        """
        Validate an Infoblox change ticket. This sanity checks inputs, but
        does not check Infoblox for existing records.

        Args:
            ticket (dict): A ticket dictionary from the ServiceNow.get_ticket_info() function.

        Returns:
            dict: A modified ticket dictionary.

        Raises:
            ValueError: If IP/MAC/FQDN do not have a recognized format.
        """
        if not helpers.has_valid_ip(ticket["ip"]):
            raise ValueError("Missing/Invalid IP")

        ticket["mac"] = helpers.parse_mac(ticket["mac"])
        if len(ticket["mac"]) == 0:
            raise ValueError("Missing/Invalid MAC")

        domain = helpers.parse_domain_name(ticket["fqhn"])
        if ticket["type"] == "Host" and len(domain) != 0:
            ticket["hostname"] = domain[0]
            ticket["zone"] = domain[1]
        elif ticket["type"] == "Host":
            raise ValueError("Missing/Invalid Domain")

        if "ip assignment req" in ticket["short_description"].lower():
            ticket["details"] = {"ip": ticket["ip"],
                    "mac": ticket["mac"], "fqdn": ticket["fqhn"]}
        else:
            ticket["details"] = {}

        return ticket

    def run(self, ticket):
        """
        Complete and apply an Infoblox ticket.

        Args:
            ticket (dict): A ticket dictionary from the ServiceNow.get_ticket_info() function.

        Returns:
            str: A result message indicating a successful ticket close.
        """
        # Create host record or assign a fixed address
        if ticket["type"] == "Host":
            domain = helpers.parse_domain_name(ticket["fqhn"])
            self.infoblox.add_hostname(ticket["ip"], domain[0], domain[1],
                    "Client (DHCP)", ticket["mac"],
                    ticketnumber=ticket.get('number'))
        else:
            self.infoblox.add_fixed_address(ticket["ip"], ticket["mac"],
                    "Client (DHCP)", ticketnumber=ticket.get('number'))

        return ("Device with MAC address {} has been assigned " +
                "the IP address {}").format(ticket["mac"], ticket["ip"])
