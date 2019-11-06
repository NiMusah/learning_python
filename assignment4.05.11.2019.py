#Assignment 4: A function that takes 4 optional parameters

#This functions attempts to calculate somebody's BMI using the Metric Method
#Height in meters and weight in kilograms

def bmicalculator4(weight=58, height=3 , patient='Musa', month='October'):

    return weight/(height**2), patient, month

print(bmicalculator4())
print(bmicalculator4(60))
print(bmicalculator4(60, 4,))
print(bmicalculator4(60, 4, 'MwendaZake'))
print(bmicalculator4(60, 4, 'MwendaZake', "December"))