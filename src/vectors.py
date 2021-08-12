import logging
from math import hypot
from typing import TypeVar


logging.debug('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
Vector = TypeVar('Vector')


class Vector:
    """
    Creating the Vector Class for initializing vectors
    """
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y
        logging.info('Initial Variables within class have been defined as {1} and {2}', format(x), format(y))

    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other: Vector) -> Vector:
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int) -> Vector:
        return Vector(self.x * scalar, self.y * scalar)


if __name__ == "__main__":
    abc = Vector(2, 4)
    bcd = Vector(4, 5)
    cde = abc+bcd
    print(abc+bcd)
    print(abc * 5)
    print(abs(abc))
    print(abc)
