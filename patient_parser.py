# Create a class to parse patient_detail images and extract useful fields
from General_parser import (MedicalDocParser)
import re

# Clean extracted with unwanted characters
def clean_match(match):
    extra_charactors = ['Birth Date', '|', '‘']
    for extra_charactor in extra_charactors:
        match = match.replace(extra_charactor, '').strip()
    return match

# Trim extracted text to only interested information
def clean_name(name):
    date_pattern = '((Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[ \d]+)'
    date_matches = re.findall(date_pattern, name)

    if date_matches:
        date = date_matches[0][0]
        name = name.replace(date, '').strip()
    return name

# Create a class to parse patient_information
class PatientParser(MedicalDocParser):
    def __init__(self, text):
        MedicalDocParser.__init__(self, text)
    # Extract 4 fields from the files: name, phone, Hepatitis B vaccination status and medical problem
    def parse(self):
        return {
            'patient_name': self.get_name(),
            'patient_phone': self.get_phone(),
            'hep_b_status': self.get_hep_b_status(),
            'medical_problem': self.get_medical_problem(),
        }

    # Define 4 functions to extract each field
    def get_name(self):
            # 1. Extract patient name
            pattern = 'Patient Information(.*?)\(\d{3}\)'
            matches = re.findall(pattern, self.text,  flags=re.DOTALL)
            if len(matches) > 0:
                match = matches[0]
                return clean_name(clean_match(match))  #get clean field of names

    def get_phone(self):
            # 2. Extract patient phone
            pattern = 'Information(.*?)(\(\d{3}\) \d{3}-\d{4})'
            matches = re.findall(pattern, self.text, flags=re.DOTALL)
            if len(matches) > 0:
            # Remove leading and trailing strings
                return matches[0][1].strip()   #get clean field of phone numbers

    def get_hep_b_status(self):
            # 3. Extract patient's hep_b_status
            pattern = 'vaccination\?(.*?)List'
      # use yes or no selection only patter = 'Have you had the Hepatitis B vaccination\?.*(Yes|No)'
            matches = re.findall(pattern, self.text, flags=re.DOTALL)
            if len(matches) > 0:
                match = matches[0]
                return clean_match(match)    #get clean field of status

    def get_medical_problem(self):
        # 4. Extract patient's hep_b_status
        pattern = 'headache(.+)'
        matches = re.search(pattern, self.text, flags=re.DOTALL)
        # Remove leading and trailing strings
        if matches:
            match = matches.group(1).strip().split('\n')[1]
            if len(match)>0:
                return match
            else:
                return matches.group(1).strip().split('\n')[2] #get clean field of status for different texts