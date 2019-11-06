#Assignment 3: A function that takes 1 required and 3 optional parameters

#This functions attempts to calculate somebody's BMI using the Metric Method
#Height in meters and weight in kilograms

def bmicalculator3(weight, height=1.8 , patient='Peter', month='November'):

    return weight/(height**2), patient, month

print(bmicalculator3(150))
print(bmicalculator3(200, 2))
print(bmicalculator3(60, 4, 'Himuselefu'))
print(bmicalculator3(60, 4, 'Herselefu', 'December'))