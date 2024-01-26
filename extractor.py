# Create a function to extract useful fields from different patient file types
from pdf2image import convert_from_path
import pytesseract
import preprocess
from prescription_parser import PrescriptionParser
from patient_parser import PatientParser

POPPLER_PATH = r'c:\users\spinc\appdata\local\programs\python\poppler-23.11.0\Library\bin'
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def extract(file_path, file_format):
    # Step 1: extracting text from pdf file
    # Extracting multiple pages
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''
    for page in pages:
        processed_image = preprocess.preprocess_image(page)
        text = pytesseract.image_to_string(processed_image, lang='eng')
        document_text += '\n' + text

# Step 2: extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientParser(document_text).parse()
    # create exception
    else:
        raise Exception(f"Invalid document format: {file_format}")
    return extracted_data

# Main routine: use 4 files as examples for patient data extraction
if __name__ == '__main__':
    patient_data1 = extract(
        'resources/patient_details/pd_1.pdf',
        'patient_details')
    patient_data2 = extract(
        'resources/patient_details/pd_2.pdf',
        'patient_details')
    prescription_data1 = extract(
        'resources/prescription/pre_1.pdf',
        'prescription')
    prescription_data2 = extract(
        'resources/prescription/pre_2.pdf',
        'prescription')
    print(prescription_data1)
    print(prescription_data2)
    print(patient_data1)
    print(patient_data2)
