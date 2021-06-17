from cryptography.fernet import Fernet
from getpass import getpass, getuser
import time


def network_ssh_account():
    """
    Creates the Keys, and stores the Username/passwords for use in scripts.
    """
    print(f"""Please Save the following Key in a secure location. This Key is for your SSH Service account PASSWORD. 
You will need to enter it at the start of each script.
This Prompt with disappear in 90 seconds""")
    while True:
        result = input(__prompt="Ready to Continue? [y/n]")
        if result != 'y' or result != 'n':
            print("Please enter a 'y' or 'n'")
        elif result == 'y':
            break
        elif result == 'n':
            return

    for count, x in enumerate(range(0, 2)):
        if count == 0:
            print(Fernet.generate_key(), end="\r")
            time.sleep(90)
        else:
            print("", end="\r")

    cipher_suite = Fernet(getpass(prompt='Enter Password Key'))
    password = cipher_suite.encrypt(getpass(prompt='Enter SSH password for Service Account'))
    with open('ssh_pass_bytes.bin', 'wb') as file_object:
        file_object.write(password)