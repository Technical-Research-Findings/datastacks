
from math import hypot
import logging
from math import hypot
import logging


logging.debug('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

class Vector:
    """
    Creating the Vector Class for initializing vectors
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        logging.info('Initial Variables within class have been defined as {1} and {2}', format(x), format(y))

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    abc = Vector(2,4)
    bcd = Vector(4,5)
    cde = abc+bcd
    print(abc+bcd)
    print(abc * 5)
    print(abs(abc))
    print(abc)

class Vector:
    """
    Creating the Vector Class for initializing vectors
    """
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        logging.info('Initial Variables within class have been defined as {1} and {2}', format(x), format(y))

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    abc = Vector(2,4)
    bcd = Vector(4,5)
    cde = abc+bcd
    print(abc+bcd)
    print(abc * 5)
    print(abs(abc))
    print(abc)