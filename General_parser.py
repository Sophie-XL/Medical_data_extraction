# Create a dummy general class for 2 children classes: prescription parser and patient information parser

import abc

class MedicalDocParser(metaclass=abc.ABCMeta):
    def __init__(self, text):
        self.text = text

    @abc.abstractmethod  #reinforce methods in a class
    def parse(self):
        pass