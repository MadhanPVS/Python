'''
Similar to wide other languages, Python has 2 different type conversions:-
1) Implicit Type Conversion - The Python interpreter has the ability to automatically converts from one data type to another without any user interactions.
2) Explicit Type Conversion - Forced by user to convert from one data type to other, there is a risk of data type violation or data loss, it is best practices to include Try/Except blocks
'''

# 1) Implicit Type Conversion
#**************************************************************************#
x = 5
print("Type of x:",type(x)) #Output: Type of x: <class 'int'>

y = 15.6
print("Type of y:",type(y)) #Output: Type of x: <class 'float'>

z = x + y
print(z) 
print("Type of z:",type(z)) #Output: Type of x: <class 'float'>
#**************************************************************************#



# 2) Explicit Type Conversion
#**************************************************************************#
# ____initializing string____
input_string = "1001"
print("Initialized String: ",input_string) #1001

# string to integer Base 2
result_int = int(input_string,2)
print ("Post conversion of string to Int: ", end="")
print (result_int) #9
 
# string to float
result_float = float(input_string)
print ("Post conversion of string to float : ", end="")
print (result_float) #1001.0

# ____initializing integers____
num1 = 24
num2 = 77
print("Initialized Integer1: ",num1) #24
print("Initialized Integer2: ",num2) #77

# integer to complex number
result_complex = complex(num1,num2)
print ("Post conversion of integer to complex number : ",end="")
print (result_complex) #(24+77j)
 
# integer to string
result_string = str(num1)
print ("Post conversion of integer to string : ",end="")
print (result_string) #24

# integer to ASCII
result_ASCII = chr(num2)
print ("Post conversion of integer to ASCII : ",end="")
print (result_ASCII) #M

# ____initializing string____
input_string = 'Python'
print("Initialized String: ",input_string) #Python
 
# string to tuple
result_tuple = tuple(input_string)
print ("Post conversion of string to tuple : ",end="")
print (result_tuple)
 
# string to set
result_set = set(input_string)
print ("Post conversion of string to set : ",end="")
print (result_set)

# string to list
result_list = list(input_string)
print ("Post conversion of string to list : ",end="")
print (result_list)

# ____initializing list____
list_of_tuples = [('a', 1), ('b', 2), ('c', 3)]
list_of_lists = [['a', 1], ['b', 2], ['c', 3]]

print("Initialized list_of_tuples: ",list_of_tuples) #Python
print("Initialized list_of_lists: ",list_of_lists) #Python

# list_of_tuples to dictionary
result_dictionary = dict(list_of_tuples)
print("Post conversion of list_of_tuples to dictionary",result_dictionary) #Output: {'a': 1, 'b': 2, 'c': 3}

# list_of_lists to dictionary
result_dictionary = dict(list_of_lists)
print("Post conversion of list_of_lists to dictionary",result_dictionary) #Output: {'a': 1, 'b': 2, 'c': 3}

# ____initializing tuple____
input_tuple = (('a', 1) ,('f', 2), ('g', 3))
print("Initialized tuple: ",input_tuple) #Python

# tuple to dictionary
result_dictionary = dict(input_tuple)
print ("Post conversion of tuple to dictionary : ",end="")
print (result_dictionary)
#**************************************************************************#


#Example: Reading a string value from user and converting it to a integer
try:
    Hours = int(input('how many hours you sleep?')) #7
except:
    print('enter a valid number')
    quit()
if(Hours == 7):
    print('You are maintaining a good sleep cycle, keep the same!')
elif(Hours > 7):
    print('You are oversleeping, which is bad for health')
else:
    print('You have to maintain a good sleep cycle, it will cause more health issues than yuo expect')