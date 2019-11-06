#Assignment 2: A function that takes 2 required and 2 optional parameters

#This functions attempts to calculate somebody's BMI using the Metric Method
#Height in meters and weight in kilograms

def bmicalculator2(height, weight, patient='Peter', month='November'):

    return weight/(height**2), patient, month

print(bmicalculator2(1.8, 150))
print(bmicalculator2(1.8, 150, 'PatientZero'))
print(bmicalculator2(1.8, 150, 'PatientZero', "January"))



