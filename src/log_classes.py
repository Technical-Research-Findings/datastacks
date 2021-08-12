import logging
import pytest

# General Guidelines for logging
log_handler = logging.FileHandler('file.log')
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class SpecialChar:
    def __init__(self, symbol:str) -> None:
        self.symbol = symbol
        logging.info(f'{symbol} has been initialized')

    def __repr__(self) -> str:
        logging.info(f'Inside the {__name__} function')
        return 'Special Character {%r}' % self.symbol

    def convert_ordinal(self) -> int:
        logging.info(f'Inside the {__name__} function')
        return ord(self.symbol)


def instance():
    return SpecialChar('#').convert_ordinal()


if __name__ == '__main__':
    print(instance())
