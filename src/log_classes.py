import logging
import pytest

# General Guidelines for logging
logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class SpecialChar:
    def __init__(self, symbol):
        self.symbol = symbol
        logging.info(f'{symbol} has been initialized')

    def __repr__(self):
        logging.info('Inside the __repr__ function')
        return 'Special Character {%r}' % self.symbol

    def convertordinal(self):
        logging.info('Inside the convertordinal function')
        return ord(self.symbol)


if __name__ == '__main__':
    print(SpecialChar('#').convertordinal())