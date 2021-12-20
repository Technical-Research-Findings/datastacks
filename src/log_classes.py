import logging
from typing import TypeVar

# General Guidelines for logging
# TODO: Implement decorators for the logging methods in python
log_handler = logging.FileHandler('file.log')
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')


SpecialChar = TypeVar('SpecialChar')
# TODO : Implement Class Methods and Static Methods.
#  Implement Getter and Setter classes


class SpecialChar:
    def __init__(self, symbol: str) -> None:
        """
        Initializing the Special Character Class.
        :param symbol: symbol
        """
        self._symbol = symbol  # making __symbol a private variable by putting in __ before it
        logging.info(f'{symbol} has been initialized')

    @property
    def symbol(self) -> str:
        """
        Getter methods for the symbol variable in SpecialChar class
        :return: self.__symbol
        """
        logging.info(f'{self._symbol} Getter method has been called')
        return self._symbol

    @symbol.setter
    def symbol(self, symbol: str):
        """
        Setter Method for the SpecialChar class
        :param symbol: The variable to set to initialize the SpecialChar class
        :return:
        """
        logging.info(f'{symbol} will be set to the SpecialChar class as the variable ')
        self._symbol = symbol

    def __repr__(self) -> str:
        """
        This is the representation of the class when it is printed out.
        :return: SpecialChar String Representation
        """
        logging.info(f'Inside the {__name__} function')
        return 'Special Character (%r)' % self._symbol

    def _convert_ordinal(self) -> int:
        """
        #Convert the Special Character to Integer (Ordinal) representation
        :return: Integer representation of the Special Character
        """
        logging.info(f'Inside the {__name__} function')
        return ord(self._symbol)

    @classmethod
    def update_symbol(cls, new_symbol: str) -> SpecialChar:
        """
        This is the update method for updating the class with the new special character
        :param new_symbol: Input Special Character to update the class with.
        :return: SpecialChar
        """
        logging.info(f'Inside the {__name__} function')
        return cls(new_symbol)

    def increment_symbol(self, cls):
        logging.info(f'Inside the {__name__} function')
        return cls(chr(ord(self._symbol) + 1))

    def ordinal_value(self) -> int:
        """
        Creating an instance method of the function to call from the main function
        :return: Integer value of the Special Character
        """
        return self._convert_ordinal()


if __name__ == '__main__':
    abc = SpecialChar('#')
    print(abc)
    abc = abc.update_symbol('$')
    print(abc.increment_symbol(SpecialChar))
