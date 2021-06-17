from netmiko import ConnectHandler
from auth import SSH
import logging

def _exception(e):
    logging.error(e)
    return

def connnect(host,device_type):
    try:
        net_connect = ConnectHandler(
            device_type=device_type,
            host=host,
            username=SSH.username,
            password=bytes(SSH.password_suite.decrypt(SSH.password)).decode("utf-8"),
        )
    except Exception as e:
        _exception(e)
    else:
        return net_connect


