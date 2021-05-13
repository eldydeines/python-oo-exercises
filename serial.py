""" Python serial number generator.
    Eldy Deines - May 13 --
"""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start):
        """Creates unique number for instance"""
        self.start = start - 1
        self.serial = self.start

    def __repr__(self):
        """Represent the class"""
        return f"<SerialGenerator start={self.start} next={self.serial+1}>"

    def generate(self):
        """Increments serial number"""
        self.serial += 1
        return self.serial

    def reset(self):
        """Resets back to the original start number provided"""
        self.serial = self.start
