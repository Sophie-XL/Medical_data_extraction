# Medical_data_extraction
This Python project focuses on medical data extraction, specifically targeting patient details and prescription information. The core functionality is implemented through a FastAPI-based API that communicates with a frontend application. The API allows users to upload medical documents in various formats, such as PDF, and extracts relevant information for further processing.

## Project Background
Medical data extraction involves the automated retrieval of pertinent information from various medical documents, such as prescriptions, patient records, and test results. This process is crucial for digitizing and organizing healthcare data, leading to improved efficiency, accuracy, and accessibility of information. Traditionally, much of this data has been stored in paper-based formats, making it challenging to analyze, share, and derive insights. Automated and standarized extraction have several benefits to the healthcare industry:
- Efficiency and time savings
- Accuracy and error reduction
- Information sharing among different healthcare systems
- Structured data for medical research
- Regulatory compliance

## Project Structure
1. Main File [`main.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/main.py)
<br>This file sets up the FastAPI application and defines an API endpoint (`/extract_from_doc`) for processing medical documents.
<br>The key steps include:
- Receiving file uploads from the frontend.
- Saving uploaded files with unique identifiers for traceability.
- Utilizing the `extract` function to extract medical information based on the file format.
- Implementing exception handling for robust error management.
2. Extractor Function [`extractor.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/main.py)
<br>This module contains the `extract` function responsible for extracting medical information from documents. It uses the `pdf2image` library to convert PDF pages into images, employs __Optical Character Recognitio (OCR)___ via `Tesseract` to extract text, and then parses the text using specialized parsers (`PrescriptionParser` and `PatientParser`).

3. Preprocess Function [`preprocess.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/preprocess.py)
<br>The `preprocess_image` function within this module is used to enhance image quality before OCR. It performs operations such as converting color images to grayscale, resizing for better contrast, and applying __adaptive thresholding__.

4. General Parser Class [`General_parser.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/General_parser.py)
<br>This module defines an abstract base class `MedicalDocParser`, which serves as the foundation for specific parsers. It enforces the implementation of the parse method in child classes.

5. Prescription Parser and Patient Parser Class [`prescription_parser.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/prescription_parser.py) [`patient_parser.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/patient_parser.py)
<br>This two classes inherit from `MedicalDocParser` and are used to parse two types of patient documents: prescription files and patient detail files. They defines methods to extract fields like patient name, address, prescriptions, directions, refill details, medical problems, etc.. Additionally, it includes cleaning functions to handle unwanted characters.<br>

6. Test Codes [`TestCode_patient.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/TestCode_patient.py) [`TestCode_prescription.py`](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/TestCode_prescription.py)   
This two files contain test cases for both `PrescriptionParser` and `PatientParser` using the `pytest` framework. It ensures that the parser functions correctly extract information from sample documents.

7. [Computer Vison Concept Notebook](https://github.com/Sophie-XL/Medical_data_extraction/blob/9774dd5a14536495583c644344d9e490160cf074/Computer%20Vision%20Concepts.ipynb)  
In this note book, I provided step by step explaination and codes for the computer vision related concepts used in the project:
- Converting PDF into images using `pdf2imge` module
- Extracting text from images using `resseract` module
- Using Simple and Adaptive Thresholding to enhance image contrst with `cv2`
- Extract fields using __Regular Expression (Regex)__

## Technical Skills Demonstrated in this Project:
- [x] __OCR__ and __Immage Processing__ techniques to extract text information from images
- [x] Development for specialized __parsers__ and implementation of cleaning functions in extracted text
- [x] __Modular Code Design__ to improve code reusability 
- [x] Application of __Test-Driven Development (TDD)__ using `pytest`
- [x] Documentation for enhanced code readability
- [x] Creation of API endpoints using `FastAPI`
- [x] API testing using `Postman`
- [x] File Handling and Exception Handling
