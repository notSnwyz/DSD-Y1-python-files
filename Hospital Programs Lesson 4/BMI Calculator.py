patientWeight = int(input("Enter the patient's weight in KG: "))
PATIENT_HEIGHT = float(input("Enter the patient's height in meters: "))

bmi = patientWeight / (PATIENT_HEIGHT * PATIENT_HEIGHT)
print("The patient's BMI is:", str(bmi))