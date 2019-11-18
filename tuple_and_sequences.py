#Question 1:
    #1.a) Create a dictionary then loop through the values in it

diction={'Noun': 'Moses', 'Verb':'Walk', 'Adverb': 'Quickly', 'Pronuon': 'They' }

for values in diction:
    print(values)

print(type(diction))


#Printing the key value pairs in the dictionary created

diction={'Noun': 'Moses', 'Verb':'Walk', 'Adverb': 'Quickly', 'Pronuon': 'They' }

for key, values in diction.items():
    print(key, '-', values)

print(type(diction))



#Question 1:
    #1.b) Create a tuple then loop through the values in it

tuple_diction=("Moses", "Walk", "Quickly", "They")

for values in tuple_diction:
    print(values)

print(type(tuple_diction))


#Question 1:
    #1.c) Create a set then loop through the values in it

set_diction={"Moses", "Walk", "Quickly", "They"}

for values in tuple_diction:
    print(values)

print(type(set_diction))








#Question 2:
    #2.a) Use input to ask for a user's name

user_name=input("Kindly provide your Name:" )
print("Your name is- "+ user_name)




#Question 2:
    #2.b) Use input to ask for a user's number

user_number=input("Kindly provide your Number:" )
print("This number is- "+ user_number)




#Question 2:
    #2.c) Create a list by asking for inputs

user_details=[]

user_name=input("Kindly provide your Name:")
user_marital_status=input("Kindly provide your marital status:")

user_details.append(user_name)
user_details.append(user_marital_status)

print(user_details)






#Question 3:
    #3.a) Create a string and cast it to a float
str_example='casting'
try:
    float(str_example)

except:
    print("Incompatible")

pass



#Question 3:
    #3.b) Create a string and cast it to a list
str_example1='casting'
try:
    list(str_example1)

except:
    print("Incompatible")

else:
    print(list(str_example1))

pass



#Question 3:
    #3.c) Create an int and cast it to a string
str_example2=2
try:
    string(str_example2)

except:
    print("3c. genarates Incompatibility")

pass



#Question 3:
    #3.d) Create a list and cast it to a string
str_example3=["How is", "this", "possible?"]
try:
    string(str_example13)

except:
    print("Incompatible")

pass



#Question 3:
    #3.e) Create a float and cast it to a string
str_example4=3.7
try:
    string(str_example14)

except:
    print("Incompatible")

pass


