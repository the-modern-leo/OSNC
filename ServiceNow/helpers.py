from builtins import range
import re
import collections

def has_valid_ip(ip):
    """
    Validates an IP address.

    Args:
        ip (str): The IP to validate.

    Returns:
        bool: True if IP follows standard conventions, False otherwise.
    """
    if (re.match(r"\d+\.\d+\.\d+\.\d+", ip) is not None):
        ip = ip.split(".")

        for ip_section in ip:
            ip_section = int(ip_section)
            if ip_section >= 0 and ip_section < 256:
                return True

    return False

def parse_mac(mac):
    """
    Returns the standard form of a MAC address
    (hexadecimals seperated by colons). Handles two common forms of MAC 
    notation. The hexadecimals without any seperation and hexadecimals seperated 
    with the hyphen character.

    Args:
        mac (str): The MAC address.

    Returns:
        str: The MAC address in standard form or an empty string if a MAC
        address cannot be determined.
    """
    parsed_mac = ""

    hyphens = re.match(r"[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-" + \
            "[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}-[A-Fa-f0-9]{2}", mac)
    standard_form = re.match(r"[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:" + \
            "[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}:[A-Fa-f0-9]{2}", mac)

    # Handles the case where a MAC is submitted without colons
    mac = mac.replace(" ", "")
    if (re.match(r"[A-Fa-f0-9]{12}", mac) is not None):
        for i in range(0, len(mac), 2):
            parsed_mac += mac[i] + mac[i + 1] + ":"

        parsed_mac = parsed_mac[:len(parsed_mac) - 1]
    # Handles the case with hyphen seperation
    elif (hyphens is not None):
        parsed_mac = mac.replace("-", ":")
    elif (standard_form is not None):
        parsed_mac = mac

    return parsed_mac

def parse_domain_name(fqdn):
    """
    Parses the FQDN for a hostname and the zone. The hostname and zone is 
    extracted from the FQDN. The FQDN should be of the form hostname.myzone.com, 
    where the zone can be one or more sub-domains.

    Args:
        fqdn (str): The Fully Qualified Domain Name.

    Returns:
        tuple: Hostname and the zone or an empty tuple if the
        hostname and zone cannot be determined.
    """
    if count_periods(fqdn) >= 2:
        fqdn = fqdn.split(".")
        host = fqdn[0]
        zone = ""
        for i in range(1, len(fqdn)):
            zone += fqdn[i] + "."

        zone = zone[:len(zone) - 1]
        return (fqdn[0], zone)

    return ()

def count_periods(fqdn):
    """
    Counts the number of periods in a string.

    Args:
        fqdn (str): The Fully Qualified Domain Name.

    Returns:
        int: Number of periods in a string.
    """
    period_count = 0
    for c in fqdn:
        if c == ".":
            period_count += 1

    return period_count
