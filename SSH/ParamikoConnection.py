from auth import SSH
import paramiko
import socket
import logging
import time
import re

command_fails = ['nvalid command at','% Incomplete command.','FAILED:']
# global helper functions


ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addHandler(ch)

def close_socket(transport):
    """

    :param transport:
    :return:
    """
    if transport:
        sock = transport.sock
        if sock:
            sock.close()
def _exception(e):
    logging.error(e)
    return

def remove_byte_strings(result):
    new_result = []
    for l in result.split("\r\n"):
        l = bytes(l,'utf-8')
        if b'\x1b' in l:
            l=l.replace(b'\x1b',b'')
        new_result.append(l.decode('utf-8'))
    return '\r\n'.join(new_result)


class Connection(object):
    """An SSH Object for managing connections to network switches and routers.

    Use SwitchAccess.login() to instantiate connection before self.send_command(), and SwitchAccess.logout() to
    destroy.

    Attributes:
        client: A Paramiko client object to handle the client information.
        channel: A Paramiko channel object that sends and receives data.
        prompt: The device prompt format as a string.
    """

    def __init__(self,ipaddress):
        self.client = None
        self.channel = None
        self.prompt = None
        self.conn = None
        self.username = SSH.username
        self.password = SSH.password
        self.ip = ipaddress


    def login(self, quick=False):
        """Log in to a SSH device.

        Args:
            router: Device IP address or DNS hostname.
            quick: Optional boolean - if True, shorten timeouts for logging in.

        Returns:
            A Connection object to continue sending and receiving data from
            the device.

        Raises:
            ValueErrors if there are problems logging in to the device.
        """
        logger.debug(f'SSH connection - {self.ip}')
        try:
            self.client = paramiko.SSHClient()
            self.client.load_system_host_keys()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            auth_retry = 0
            # make two login attempts, in case something strange happens
            while auth_retry < 2:
                try:
                    self.client.connect(self.ip, username=self.username,
                                   password=self.password, look_for_keys=False,
                                   allow_agent=True, timeout=(30 if quick else 240),auth_timeout=240,
                                        banner_timeout=240)
                    break  # successful

                except socket.timeout:
                    raise IOError("Connection timed out")
                except paramiko.ssh_exception.NoValidConnectionsError as N:
                    logger.error("username not exists")
                    logger.error(N, exc_info=True)
                    raise
                except paramiko.ssh_exception.AuthenticationException as a:
                    if auth_retry < 2:
                        auth_retry += 1
                        time.sleep(2)
                    else:
                        logger.error('Password incorrect: ' + str(a))
                        close_socket(self.client.get_transport())
                        raise IOError("Cannot log in to device (" + str(a) + ")")
                # except paramiko.ssh_exception as g:
                #     if "Illegal info request from server" in g:
                #         raise ConnectionError(
                #             f"Cannot log into device {self.ip} You might need to change your password\r\n"
                #             f"{g}")
                except socket.gaierror as g:
                    logger.info(f'Router Value was not found on network: {self.ip}')
                    logger.error(g, exc_info=True)
                    _exception(g)
                    raise
                except EOFError as f: #Chipher issues, or algorithms to use for connection
                    logger.error(f, exc_info=True)
                    _exception(f)
                    raise
                except Exception as e:
                    logger.error(e, exc_info=True)
                    _exception(e)
                    raise

            if auth_retry >= 2:
                close_socket(self.client.get_transport())
                raise IOError(f"Cannot log in to device: {self.ip} (TACACS user expired?)")

            self.channel = self.client.invoke_shell(height=60, width=120)
            self.channel.settimeout((30 if quick else 240))
            header = self.channel.recv(4096)  # clear self.channel
            header = header.decode("utf-8")
            timeout = 480
            count = 0
            while ('#' not in header and '>' not in header and
                   not self.channel.recv_ready()):
                count += 1
                if count > timeout: # timeout for unknown prompts
                    break
                time.sleep(0.1)  # wait for login to be successful
                if 'Duo two-factor login for' in header: #
                    break
                header += self.channel.recv(4096).decode("utf-8")
            if self.channel.recv_ready():
                header = self.channel.recv(4096).decode("utf-8")

            if '#' not in header and '>' not in header:  # invalid prompt
                time.sleep(2)  # prompt may have not loaded yet
                header += self.channel.recv(4096).decode("utf-8")
                if "Duo two-factor login for" in header:
                    return
                if '#' not in header and '>' not in header:

                    logger.info(header)
                    if self.channel is not None:
                        self.channel.close()
                    if self.client is not None:
                        self.client.close()
                    raise ValueError("Cisco prompt not reached")

            prompt = header.splitlines()[-1].strip()
            self.prompt = prompt
            self.update_prompts(self.prompt)
        except paramiko.ssh_exception.NoValidConnectionsError as N:
            raise
        except OSError as O:
            logger.error(O, exc_info=True)
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise

    def logout(self):
        """Log out of a router and clean up (close channel and socket).

        Args:
            connection: Connection object to close.
        """
        if self.channel is not None:
            self.channel.send("exit\n")
            self.channel.close()
        if self.client is not None:
            self.client.close()
            transport = self.client.get_transport()
            if transport:
                sock = transport.sock
                if sock:
                    sock.close()
        if not self.conn:
            return
        return
    def update_prompts(self,prompt):
        try:
            self.prompt = prompt + '#'
            if len(self.prompt) > 20:
                self.configprompt = prompt[:20]
                self.configprompt = self.configprompt + '(config)#'
            else:
                self.configprompt = re.sub('#', '(config)#', prompt)
            if len(prompt) > 20:
                self.configifprompt = prompt[:20]
                self.configifprompt = self.configifprompt + '(config-if)#'
            else:
                self.configifprompt = re.sub('#', '(config-if)#', prompt)
            if len(prompt) > 20:
                self.configifrangeprompt = prompt[:20]
                self.configifrangeprompt = self.configifrangeprompt + '(config-if-range)#'
            else:
                self.configifrangeprompt = re.sub('#', '(config-if-range)#', prompt)
        except Exception as e:
            _exception(e)
            raise
        else:
            pass
    def _apply_backspaces(self, device_output):
        """Apply backspace characters for devices that use them (remove the
        previous character and the backspace character).

        Args:
            device_output: Input string.

        Returns:
            A cleaned-up string.
        """
        new_output = []
        for ch in device_output:
            if ch == '\b':
                del new_output[-1:]  # this works if the list is empty as well
            else:
                new_output.append(ch)
        return ''.join(new_output)

    def enable_cisco(self, password):
        """Raises enable privilege on a Cisco device.

        Args:
            password: A string containing the enable password.

        Raises:
            ValueError if unknown output is encountered, or the enable
            command was not successful.
        """
        logger.info('Checking if in Enable Mode')
        try:
            self.channel.send("enable\n")
            while True:
                while not self.channel.recv_ready():
                    time.sleep(0.1)
                if self.channel.recv_stderr_ready():  # error was raised
                    raise ConnectionError(self.channel.recv_stderr(32768).decode("utf-8"))
                else:
                    output = self.channel.recv(4096).decode("utf-8")
                    if '#' in output:  # already enabled end the function
                        logging.info('Already Enabled')
                        break
                    if 'password' in output or 'password' in output.lower():
                        logging.info("not enabled, asking for password")
                        self.channel.send(password + "\n")
                        while not self.channel.recv_ready():
                            time.sleep(0.1)
                            if self.channel.recv_stderr_ready():  # error was raised
                                 raise ConnectionError(f"{self.channel.recv_stderr}")
                        output = self.channel.recv(4096).decode("utf-8")
                        if not output.endswith('#'):
                            raise ValueError('Enable prompt not reached: ' + output)
                        else:
                            logging.info('Successfully enabled')
                            break
                    else:
                        if "Invalid command at \'^\' marker" in output:  # already in enable mode
                            logging.info('Already Enabled')
                            break
                        if self.prompt in output:  # already in enable mode
                            logging.info('Already Enabled')
                            break

        except Exception as e:
            logger.info(f'Enable - FAILED')
            logger.error(e, exc_info=True)
        else:
            logger.info(f'Enable - Success')

    def send_command(self, command, trim=True, manypages=False, adtranmore=False,File_transfer=False):
        """Send a command to the SSH'd device.

        Args:
            command: Command string to send to the device. Note that the newline
                character should NOT be in this string.
            trim: A Boolean that determines the output format. If set to True,
                remove the sent command and returned prompt from the output.
            manypages: If True, collect more page info before detecting loops.
            adtranmore: If true, will explicitly search for a more and not a
                prompt message, as required by the adtran gear

        Returns:
            A multiline string of the command output from the device.

        Raises:
            ValueError for stuck loops (prompt not reached) or invalid commands.
        """
        logger.debug(f'Command:{command}')
        try:
            if self.channel.recv_ready():
                pass
            # ensures the channel is able to send before sending commands.
            if self.channel.send_ready():
                self.channel.send(command + "\n")
            else:
                raise ConnectionError

            loop_counter_more = 0
            output = ""
            if command == 'yes' or command == 'y':  # don't expect a prompt back
                return ''

            while True:
                # note: only check first 20 characters or whole system name,
                # since config mode truncates name at 20 chars
                # also check for [confirm]
                prompt_end = min(len(self.prompt) - 2, 20)
                loop_counter = 0
                while not self.channel.recv_ready():
                    logger.debug(f'Waiting for Response: {loop_counter}')
                    time.sleep(0.1)
                    loop_counter += 1
                    if output == '':
                        continue
                    if (self.prompt[:prompt_end] in output.splitlines()[-1] or
                            '[confirm]' in output.splitlines()[-1].rstrip() or
                    self.configprompt in output.splitlines()[-1] or
                    self.configifprompt in output.splitlines()[-1] or
                    self.configifrangeprompt in output.splitlines()[-1]):
                        break  # loop conditional and exit
                    if File_transfer:
                        if loop_counter > 4800:
                            # stuck for more than 60 seconds, give up
                            raise ValueError("Stuck in wait loop, " + str(output))
                    if loop_counter > 1200:  # stuck for more than 60 seconds, give up
                        raise ValueError("Stuck in wait loop, " + str(output))

                output += self.channel.recv(32768).decode("utf-8")
                logger.debug(f'Loop Count:{loop_counter} - {output}')
                # checks for any errors send to the channel
                if self.channel.recv_stderr_ready():
                    raise ConnectionError(self.channel.recv_stderr(32768).decode("utf-8"))

                # removes the command from the response if present or the prompt plus command
                if f'{self.prompt} {command}' in output:
                    output = re.sub(f'{self.prompt} {command}', '', output)
                if f'{self.configprompt} {command}' in output:
                    output = re.sub(f'{self.configprompt} {command}', '', output)
                if f'{self.configifprompt} {command}' in output:
                    output = re.sub(f'{self.configifprompt} {command}', '', output)
                if f'{self.configifrangeprompt} {command}' in output:
                    output = re.sub(f'{self.configifrangeprompt} {command}', '', output)
                elif command in output:
                    output = re.sub(f'{command}', '', output)
                elif f'{command}\r\n' in output:
                    output = re.sub(f'{command}\r\n', '', output)
                elif f'{command}\r' in output:
                    output = re.sub(f'{command}\r', '', output)

                if output == '':
                    continue

                if ('nvalid command at' in output.splitlines()[-3:] or
                        (len(output.splitlines()) > 1 and 'nvalid command at' in
                         output.splitlines()[-2])):
                    raise ValueError('invalid command')  # catch Cisco errors
                elif "^\r\n% Invalid command at \'^\' marker." in output:
                    break
                # stops the recieving loop when the full message has been received
                if (self.prompt[:prompt_end] in output.splitlines()[-1] or
                        '[confirm]' in output.splitlines()[-1].rstrip() or
                        self.configprompt in output.splitlines()[-1] or
                        self.configifprompt in output.splitlines()[-1] or
                        self.configifrangeprompt in output.splitlines()[-1]):
                    break # loop conditional and exit

                if ('--more--' in output.splitlines()[-1].lower() or '<--- more --->' in output.splitlines()[-1].lower()):
                    loop_counter_more += 1
                    if loop_counter_more > (400 if manypages else 100):
                        # stuck for more than 100 pages, give up
                        raise ValueError("Stuck in --more-- loop, " + str(output))
                    self.channel.send(" ")  # page through --More--
                elif 'over write?' in output.splitlines()[-1].lower():
                    self.channel.send("\n")
                elif '[yes/no]' in output.splitlines()[-1].lower():
                    break  # confirm
                elif 'Do you want to proceed? [y/n]' in output.splitlines()[-1]:
                    break
                elif 'destination filename' in output.splitlines()[-1].lower():
                    return output.replace('\b', '')
                elif 'display filename [packages.conf]?' in output.splitlines()[-1].lower():
                    break
                # waits 10 minutes for file transfer to finish
                elif '!' in output.splitlines()[-1].lower():
                    loop_counter_more += 1
                    if File_transfer:
                        if loop_counter > 4800:
                            # stuck for more than 40 minutes, give up
                            raise ValueError("Stuck in wait loop, " + str(output))
                    if loop_counter_more > 2400:
                        # wait 40 minutes for file to transfer
                        raise ValueError("file download taking too long, " + str(output))
                    self.channel.send(" ")
                # waits 10 minutes for clean switch command to finish
                elif 'this operation may take several minutes...' in output.splitlines()[-1].lower():
                    loop_counter_more += 1
                    if loop_counter_more > 6000:
                        # wait 10 minutes for file to transfer
                        raise ValueError("file download taking too long, " + str(output))
                    self.channel.send(" ")
                # waits for the full install response to be sent
                elif ('expanding image file:' in output.splitlines()[-1].lower() or
                      'package install switch all file flash' in output.splitlines()[-1].lower() or
                      'starting install local lock acquisition on switch 1' in output.splitlines()[-1].lower()):
                    loop_counter_more += 1
                    if loop_counter_more > 2400:
                        # wait 40 minutes for file to transfer
                        raise ValueError("iso install taking too long, " + str(output))
                    self.channel.send(" ")
                elif 'Delete' in output.splitlines()[-1].lower():
                    self.channel.send("y")
                elif 'FAILED:' in output.splitlines()[-1]:
                    raise ValueError(f'{output.splitlines()[-1]}')
                elif '% Incomplete command.' in output.splitlines()[-1]:
                    raise ValueError(f'unable to run command: {command}')

            if trim:
                output = output[output.find('\n') + 1:output.rfind('\n')].lstrip()

            # remove the more in the output
            output = re.sub("\[7m--More--\[m", '', output)
            output = re.sub('--More--', '', output)
            output = re.sub('<--- More --->', '', output)
            logger.debug(f'{output}')
            return remove_byte_strings(output.replace('\b', ''))

        except IndexError as I:
            logger.debug(f'Output: {output}')
            logger.debug(f'Prompt: {self.prompt}')
            logger.debug(f'Prompt length: {prompt_end}')
            logger.error(I, exc_info=True)
            _exception(I)
            raise
        except Exception as e:
            logger.error(e, exc_info=True)
            _exception(e)
            raise


