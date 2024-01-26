# Create text functions to test the prescription_parser class
from prescription_parser import PrescriptionParser
import pytest

# Input two documents used for testing
@pytest.fixture()
def doc_1_maria():
    document_text = '''
Dr John Smith, M.D
2 Non-Important Street,
New York, Phone (000)-111-2222

Name: Marta Shararpova Date: 5/11/2022

Address: 9 tennis court, new Russia, DC

K

Prednisone 20 mg
Lialda 2.4 gram

Directions:

Prednisone, Taper 5 mig every 3 days,
Finish in 2.5 weeks a
Lialda - take 2 pill everyday for 1 month

Refill: 2 times
'''
    return PrescriptionParser(document_text)

@pytest.fixture()
def doc_2_virat():
    document_text = '''
Dr John >mith, M.D

2 Non - Important street,
New York, Phone(900) - 323 - ~2222

Name: Virat Kohli Date: 2 / 05 / 2022

Address: 2 cricket blvd, New Delhi

| Omeprazole 40 mg

Directions: Use two tablets daily for three months

Refill: 3 times
'''

    return PrescriptionParser(document_text)

# Add an empty document for extreme situations
@pytest.fixture()
def doc_3_empty():
    return PrescriptionParser('')

# Test prescription_parser with pytest
def test_get_name(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_name()=='Marta Shararpova'
    assert doc_2_virat.get_name() == 'Virat Kohli'
    assert doc_3_empty.get_name() == None


def test_get_address(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_address()=='9 tennis court, new Russia, DC'
    assert doc_2_virat.get_address() == '2 cricket blvd, New Delhi'
    assert doc_3_empty.get_address() == None

def test_get_prescription(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_medicine()=='Prednisone 20 mg\nLialda 2.4 gram'
    assert doc_2_virat.get_medicine() == 'Omeprazole 40 mg'
    assert doc_3_empty.get_medicine() == None

def test_get_direction(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_direction()=='Prednisone, Taper 5 mig every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert doc_2_virat.get_direction() == 'Use two tablets daily for three months'
    assert doc_3_empty.get_direction() == None

def test_get_refill(doc_1_maria, doc_2_virat, doc_3_empty):
    assert doc_1_maria.get_refill()=='2'
    assert doc_2_virat.get_refill() == '3'
    assert doc_3_empty.get_refill() == None

def test_parse(doc_1_maria, doc_2_virat, doc_3_empty):
    record_maria = doc_1_maria.parse()
    assert record_maria['patient_name'] == 'Marta Shararpova'
    assert record_maria['patient_address'] == '9 tennis court, new Russia, DC'
    assert record_maria['patient_prescription'] == 'Prednisone 20 mg\nLialda 2.4 gram'
    assert record_maria['direction'] == 'Prednisone, Taper 5 mig every 3 days,\nFinish in 2.5 weeks a\nLialda - take 2 pill everyday for 1 month'
    assert record_maria['refill'] == '2'

    record_virat = doc_2_virat.parse()
    assert record_virat['patient_name'] == 'Virat Kohli'
    assert record_virat['patient_address'] == '2 cricket blvd, New Delhi'
    assert record_virat['patient_prescription'] == 'Omeprazole 40 mg'
    assert record_virat['direction'] == 'Use two tablets daily for three months'
    assert record_virat['refill'] == '3'

    record_empty = doc_3_empty.parse()
    assert record_empty['patient_name'] == None
    assert record_empty['patient_address'] == None
    assert record_empty['patient_prescription'] == None
    assert record_empty['direction'] == None
    assert record_empty['refill'] == None