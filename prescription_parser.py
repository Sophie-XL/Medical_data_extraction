# Create a class to parse prescription type images and extract useful fields
from General_parser import (MedicalDocParser)
import re

# Clean extracted with unwanted characters
def clean_match(match):
    extra_charactors = ['K', '|', '‘']
    for extra_charactor in extra_charactors:
        match = match.replace(extra_charactor, '').strip()
    return match

# Create a class to parse prescription
class PrescriptionParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)

    def parse(self):
        return  {
            'patient_name': self.get_name(),
            'patient_address': self.get_address(),
            'patient_prescription': self.get_medicine(),
            'direction': self.get_direction(),
            'refill': self.get_refill()
        }

    # Define parsers to get different fields
    def get_name(self):
        # 1. Extract patient name
        pattern = 'Name:(.*)Date:'
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
        # Remove leading and trailing strings
            return matches[0].strip()

    def get_address(self):
        # 2. Extract patient address
        pattern = 'Address:(.*)\n'
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
        # Remove leading and trailing strings
            return matches[0].strip()

    def get_medicine(self):
        # 3. Extract patient's prescriptions
        pattern = 'Address[^\n]*(.*)Directions'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        # Remove leading and trailing strings
        if len(matches) > 0:
            match = matches[0]
            return clean_match(match)   #get clean field of prescriptions

    def get_direction(self):
        # 4. Extract prescriptions derection
        pattern = 'Directions\:*(.*)Refill'
        matches = re.findall(pattern, self.text, flags=re.DOTALL)
        if len(matches) > 0:
            # Remove leading and trailing strings
            return matches[0].strip()

    def get_refill(self):
        # 5. Extract prescriptions refills
        pattern = 'Refill:(.*)times'
        matches = re.findall(pattern, self.text)
        if len(matches) > 0:
            # Remove leading and trailing strings
            return matches[0].strip()