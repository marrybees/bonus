class Disease:
    def __init__(self, ID, name):
        self.ID = ID
        self.name = name

    def __str__(self):
        return f" ID is{self.ID}, Name is  {self.name}"


class Doctor:
    def __init__(self, firstname, lastname, department):
        self.firstname = firstname
        self.lastname = lastname
        self.department = department
        self.patients = []

    def __str__(self):
        return f"Doctor is{self.firstname} lastname is  {self.lastname}, Department is{self.department}"

    def add_patient(self, patient):
        self.patients.append(patient)
class Patient:
    def __init__(self, piradinomaeri, saxeli):
        self.piradinomaeri = piradinomaeri
        self.saxeli = saxeli
        self.diseases = []

    def __str__(self):
        return f"Patient is  {self.saxeli},  piradinomaeri is  {self.piradinomaeri}, Diseases is {self.diseases},"

    def diagnosis(self, disease, doctor):
        self.diseases.append(disease)
        if doctor:
            self.doctor = doctor
            doctor.add_patient(self)
doqtor  = Doctor('saxeli','gvari','departamenti')
disease = Disease('985623','pacienti')
print(disease)
print(doqtor)
x = Patient('01225632','name')
print(Patient.diagnosis())
#homework2
import requests
from bs4 import BeautifulSoup
url = 'https://finance.yahoo.com/quote/FSLR?p=FSLR&.tsrc=fin-srch'
r = requests.get(url)
print(r.status_code)
content = r.text
soup = BeautifulSoup(content, 'html.parser')
body = soup.find("body")
