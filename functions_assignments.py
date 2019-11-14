# #Question 1:
# #Define a function that takes a list as a parameter and prints out all the values in the list 

# test=list(range(10))

# def print_list(test):
#     for item in test:
#         print(item)

# print_list(test)




# #Question 2:
# #Create an empty list then define a function that takes in 4 parameters and then appends values to the empty list

# emp_list=[]
# #sample_parameters=["if statements","for statements","keyword arguements","break_continue"]

# def manip_list(a,b,c,d):

#     emp_list.append(a)
#     emp_list.append(b)
#     emp_list.append(c)
#     emp_list.append(d)
    
# manip_list("if statements","for statements","keyword arguements","break_continue")
# print(emp_list)





# # #Question 3
# #     #Question 3.a: Define a filled list and a subsequent function that appends a value to it


# # filled_list=list(range(10))

# # def append_function(filled_list):

# #     filled_list.append('value10')
# #     print(filled_list)

# # append_function(filled_list)



# #Question 3:Correction
#     #Question 3.a: Define a filled list and a subsequent function that appends a value to it


# filled_list=list(range(10))

# def append_function(value):

#     filled_list.append(value)
#     print(filled_list)

# append_function(20)




#Question 3:Correction2
    #Question 3.a: Define a filled list and a subsequent function that appends a value to it


filled_list=list(range(10))

def append_function(filled_list, value):

    filled_list.insert(0,value)
    print(filled_list)

append_function(filled_list,20)







# # #Question 3
#     #Question 3.b: Define a filled list and a subsequent function that inserts a value to it

# filled_list=list(range(10))

# def insert_function(filled_list):

#     filled_list.insert(0,'value1')
#     print(filled_list)

# append_function(filled_list)





# # #Question 3
#     #Question 3.c: Define a filled list and a subsequent function that removes a value to it

# filled_list=list(range(10))

# def remove_function(filled_list):

#     filled_list.remove(9)
#     print(filled_list)

# append_function(filled_list)





# # #Question 3
#     #Question 3.d: Define a filled list and a subsequent function that clears the created list

# filled_list=list(range(10))

# def clear_function(filled_list):

#     filled_list.clear()
#     print(filled_list)

# append_function(filled_list)
