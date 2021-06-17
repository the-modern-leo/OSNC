class Interfaces:

    """Iterator that starts on the first interface of a switch (1/0/1 or 0/1) and counts up till the last interface"""

    def __init__(self, start):
        self.start_interface = start

    def __iter__(self):
        return self

    def __next__(self):
        num = self.num
        self.num += 1
        return num