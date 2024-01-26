# Create text functions to test the patient_parser class
from patient_parser import PatientParser
import pytest

# Input two documents used for testing
@pytest.fixture()
def doc_1_jerry():
    document_text = '''
Patient Medical Record

Patient Information Birth Date

Jerry Lucas May 2 1998

(279) 920-8204 Weight:

4218 Wheeler Ridge Dr 57

Buffalo, New York, 14201 Height:

United States gnt
170

In Case of Emergency

eee

Joe Lucas . 4218 Wheeler Ridge Dr
Buffalo, New York, 14201
Home phone United States
Work phone

General Medical History

Chicken Pox (Varicelia): Measles: ..

IMMUNE NOT IMMUNE

Have you had the Hepatitis B vaccination?
‘Yes

| List any Medical Problems (asthma, seizures, headaches):
N/A

7?
v

17/12/2020
_—

Name of Insurance Company:
Random Insuarance Company

Policy Number:
5638746258

Do you have medical insurance?

_ Yes

Medical Insurance Details

List any allergies:
N/A

List any medication taken regularly:

N/A

4218 Smeeler Ridge Dr
Buffalo, New York, 14206
United States

Expiry Date:
31 December 2020
'''
    return PatientParser(document_text)

@pytest.fixture()
def doc_2_kathy():
    document_text = '''
17/12/2020

Patient Medical Record

Patient Information Birth Date
Kathy Crawford May 6 1972
(737) 988-0851 Weight’
9264 Ash Dr 95
New York City, 10005 .
United States Height:
190
In Casc of Emergency
7 ee
Simeone Crawford 9266 Ash Dr
New York City, New York, 10005
Home phone United States
(990) 375-4621
Work phone

Genera! Medical History

a

a

a ea A CE i a

Chicken Pox (Varicella): Measies:

IMMUNE IMMUNE

Have you had the Hepatitis B vaccination?
No

List any Medical Problems (asthma, seizures, headaches}:

Migraine

be

CO
nat
aa
oo
.

‘Name of Insurance Company:

Random Insuarance Company - 4789 Bollinger Rd
Jersey City, New Jersey, 07030

a Policy Number:
ra 1520731 3 Expiry Date:

. 30 December 2020
Do you have medical insurance?

Yes:

Medical Insurance Details

List any allergies:

Peanuts

List any medication taken regularly:
Triptans
'''

    return PatientParser(document_text)

# Add an empty document for extreme situations
@pytest.fixture()
def doc_3_empty():
    return PatientParser('')

# Test patient_parser with pytest
def test_get_name(doc_1_jerry, doc_2_kathy, doc_3_empty):
    assert doc_1_jerry.get_name() =='Jerry Lucas'
    assert doc_2_kathy.get_name() == 'Kathy Crawford'
    assert doc_3_empty.get_name() == None

def test_get_phone(doc_1_jerry, doc_2_kathy, doc_3_empty):
    assert doc_1_jerry.get_phone() =='(279) 920-8204'
    assert doc_2_kathy.get_phone() == '(737) 988-0851'
    assert doc_3_empty.get_phone() == None

def test_get_hep_b_status(doc_1_jerry, doc_2_kathy, doc_3_empty):
    assert doc_1_jerry.get_hep_b_status() =='Yes'
    assert doc_2_kathy.get_hep_b_status() == 'No'
    assert doc_3_empty.get_hep_b_status() == None

def test_get_medical_problem(doc_1_jerry, doc_2_kathy, doc_3_empty):
    assert doc_1_jerry.get_medical_problem() =='N/A'
    assert doc_2_kathy.get_medical_problem() == 'Migraine'
    assert doc_3_empty.get_medical_problem() == None

def test_parse(doc_1_jerry, doc_2_kathy, doc_3_empty):
    record_jerry = doc_1_jerry.parse()
    assert record_jerry['patient_name'] == 'Jerry Lucas'
    assert record_jerry['patient_phone'] == '(279) 920-8204'
    assert record_jerry['hep_b_status'] == 'Yes'
    assert record_jerry['medical_problem'] == 'N/A'

    record_kathy = doc_2_kathy.parse()
    assert record_kathy['patient_name'] == 'Kathy Crawford'
    assert record_kathy['patient_phone'] == '(737) 988-0851'
    assert record_kathy['hep_b_status'] == 'No'
    assert record_kathy['medical_problem'] == 'Migraine'

    record_empty = doc_3_empty.parse()
    assert record_empty['patient_name'] == None
    assert record_empty['patient_phone'] == None
    assert record_empty['hep_b_status'] == None
    assert record_empty['medical_problem'] == None