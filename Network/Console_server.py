from auth import SSH

class Console_server:
    def __init__(self,ip):
        self.ip = ip
        self.conn = None

    def __enter__(self):
        cisco_881 = {
            'device_type': 'invalid',
            'host': self.ip,
            'username': SSH.username,
            'password': SSH.password,
            'port': 22,  # optional, defaults to 22
            'secret': '',  # optional, defaults to ''
        }
        self.conn = SSH(self.ip)
        self.conn = self.conn.login()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.conn:
            self.conn.disconnect()
