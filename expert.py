from experta import *
class MedicalExpert(KnowledgeEngine):
@Rule(Fact(symptom="fever"))
def has_fever(self):
print("Patient has a fever.")
@Rule(Fact(symptom="cough"))
def has_cough(self):
print("Patient has a cough.")
@Rule(Fact(symptom="fever") & Fact(symptom="cough"))
def flu_diagnosis(self):
print("Diagnosis: The patient may have the flu.")
@Rule(Fact(symptom="headache"))
def has_headache(self):
print("Patient has a headache.")
@Rule(Fact(symptom="headache") & Fact(symptom="stiff neck"))
def meningitis_diagnosis(self):
print("Diagnosis: The patient may have meningitis. Seek medical attention immediately.")
# Create an instance of the expert system
engine = MedicalExpert()
# Reset and declare facts (symptoms)
engine.reset()
engine.declare(Fact(symptom="fever"))
engine.declare(Fact(symptom="cough"))
# Run the expert system
engine.run()
