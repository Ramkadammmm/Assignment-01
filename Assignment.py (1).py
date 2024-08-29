#!/usr/bin/env python
# coding: utf-8

# # Q.1) Explain the key features of Python that make it a popular choice for programming

# Python is Popular Language beacuse of Following reasons.
# 
# 1) Free and Open Source
# 2) Python is dynamic Language
# 3) Easy to code
# 4) Easy to read
# 5) Object Oriented Language
# 6) Large Community Support
# 7) Frontend and backend development
# 
#  Some more Advanteages of Python language
# 
# 1) Extensive support libraries
# 2) Dynamically typed language
# 3) Object-Oriented and Procedural programming language
# 

# # Q.2) Describe the Role of predefined keywords in Python and provide examples of how they are used in a Program
# 

# In Python, Predefined keywords are reserved words that have special meaning and cannot be used as identifiers,
# These keywords are integral to the Python language syntax and define its structure and control flow

# In[1]:


#if :-  Used to make decisions in code. It executes a block of code if its condition is true.
#Example of If

a = 10
b = 20
if a < b:
    print("a is less than b")


# In[2]:


# else :-to define a block of code that runs when the if condition is false.
# example of else

a = 20
if a > 15:
    print("a is grater than 15")
else:
    print("a is less than 15")


# In[3]:


#elif :- In short of else if,it allows multiple conditions to be checked sequentially
# Example of elif
x = 20
if x > 30:
    print("x is greater than 30")
elif x > 5:
    print("x is greater than 20 but not greater than 30")
else:
    print("x is 20 or less")


# # Loops 

# :- Used to create a loop that iterates over a sequence 

# While Loops :- Creates a loop that continues to execute as long as its condition is true.
# 

# In[4]:


count = 0
while count < 5:
    print(count)
    count += 1


# For Loops : - Used to create a loop that iterates over a sequence.
# 

# In[5]:


flowers = ["Rose", "Mogra", "sunflower"]
for flowers in flowers:
    print(flowers)


# import:- Imports modules or specific attributes from modules into the current namespace.
# 

# In[6]:


import math
print(math.sqrt(20))


# # Q.3) Compare and contrast mutable and immutable obects in Python with example

# Mutable Objects :- Mutable objects are those whose state or value can be changed after they are created.

# Examples: 1) List , 2) Dictionaries , 3) Sets 

# 1) Lists:-  Lists can be changed by adding, removing, or altering elements.

# In[7]:


#Example of list
l = ["pwskills", "PW wallah", "Aalakh sir", "Python"]
l


# In[8]:


l.append("GATE") # Add New Elements
l 


# 2) Dictionaries :- 
# Dictionaries can be modified by adding, removing, or changing key-value pairs.

# In[9]:


my_dict = {'a': 1, 'b': 2}
my_dict['b'] = 3  # Modifies the value for key 'b'
my_dict['c'] = 4  
print(my_dict)  


# 3. Sets:- Sets can be altered by adding or removing elements.
# 

# In[10]:


set1 = {1, 2, 3}
set1.add(4)  # Adds a new element
set1.remove(2)  # Removes an element
print(set1)  


# Immutable Objects : - Immutable objects are those whose state or value cannot be changed once they are created.

# 1) Tuples:- Tuples cannot be modified after creation, their content remains fixed.
# 

# In[11]:


tuple1 = (1, 2, 3)
#tuple1[1] = 20 it can not change, it will give an error, if we try to add 
print(tuple1)  


# 2) Strings:- trings are immutable; any operation that seems to modify a string will instead create a new string.

# In[12]:


my_string = "hello"
new_string = my_string.upper()  # Creates a new string
print(new_string)  # Output: "HELLO"
print(my_string)  # Output: "hello" (original string remains unchanged)


# Comparison
# 
# 1) Mutable Objects: Can be modified after creation.
# 2) Immutable Objects: Cannot be modified after creation; any change results in a new object.
# 
# a) Memory Usage:
# 
# 1) Mutable Objects: Can be more memory-efficient in some cases since they can be changed in place.
# 2) Immutable Objects: Might use more memory if many variations of similar objects are created, as each change results in a new     object.
# 
# b) Safety:
# 
# 1) Mutable Objects: Can lead to unintended side effects if shared across different parts of the code.
# 2) Immutable Objects: Provide greater safety for concurrent programming and can be more predictable as their state cannot be altered unexpectedly.
# 
# c) Performance:
# 
# 1) Mutable Objects: Often involve less overhead for changes since they are modified in place.
# 2) Immutable Objects: May incur overhead when creating new objects for every modification, but can benefit from optimizations like interning

# # Q.4) Discuss the different types of operators in Python and provide examples of how they are used

# Operators in python : - In Python, operators are special symbols used to perform operations on values or variables. 

# 1. Arithmetic Operators ( + , - , * , % . / )
# 

# In[13]:


#Examples
a = 10
b = 20
c = a + b
print(c)


# In[14]:


c = b - a
print(c)


# In[15]:


c = b/a
print(c)


# In[16]:


c = a*b
print(c)


# 2. Comparison Operators

# These operators compare values and return a boolean result

# In[17]:


#Equal to (==):
a = 10
b = 10
a == b


# In[18]:


# a is greater than b 
a < b


# In[19]:


# a is less than b 
a != b


# In[20]:


# a is eqaul or greater than b
a >= b


# 3. Logical Operators
# 
# These operators are used to perform logical operations.

# In[21]:


# And (and): Returns True if both conditions are true.
a = 10 
b = 20
(a != b) and (b > a)


# In[22]:


# Or: Returns True if at least one condition is true.
a = 10
b = 20
(a != b) or (a == b)


# In[23]:


# Not (not): Returns True if the condition is false.
a = 5
b = 10
c = print(not(a < b))


# 4. Assignment Operators : -
# These operators are used to assign values to variables.

# In[24]:


#Assignment (=): Assigns a value to a variable.
x = 5
print(x)    


# In[25]:


#Addition assignment (+=): Adds a value to the variable and assigns the result.
x += 8
x


# In[26]:


#Subtraction assignment (-=): Subtracts a value from the variable and assigns the result.
a -= 5
a


# In[27]:


#Multiplication assignment (*=): Multiplies the variable by a value and assigns the result.
a *= 25
a


# In[28]:


x *= 4  
x


# In[29]:


#Modulus assignment (%=): Applies the modulus operation and assigns the result.
x %= 5 
x


# 5. Bitwise Operators :- 
# These operators perform bit-level operations.

# 6. Membership Operators :- 
# These operators test for membership within a collection.

# 7. Identity Operators :- 
# These operators compare the memory location of two objects.

# # Q.5) Explain the concept of type casting in Python with examples

# Type casting : - In Python Type Casting refers to the process of convrting a value from one data type to another data type

# Python provides built-in functions for type casting, which allow you to explicitly convert values between types

# In[30]:


# 1. int() :- Converts a value to an integer.
Value = 3.0
print(int(Value))


# In[31]:


# 2. float() : - Converts a value to a float.
value_1 = 5
print(float(value_1))


# In[32]:


# 3. str() :- Converts a value to a string.
pw = 123654
pw


# In[33]:


# 4. list() :- Converts a value to a list.
success = "PWSkills"
success = list(success)
print(success)


# In[34]:


# 5. tuple() : -  Converts a value to a tuple.
a = "pwskills"
a1 = tuple(a)
print(a1)


# In[35]:


# 6. set() : - Converts a value to a set
list = [1, 2, 3, 4, 5,]
list_1 = set(list)
print(list_1)


# In[36]:


# 7. dict() : - Converts a sequence of key-value pairs into a dictionary.
a =  [('a', 1), ('b', 2)]
a1 = dict(a)
print(a1)


# In[37]:


keys = ['name', 'age']
values = ['Alice', 30]
dict_value = dict(zip(keys, values))
print(dict_value)


# # Q.6) How do conditional statements work in Python? Illustrate with examples

# Conditional statements in Python are used to make decisions in code based on certain conditions.

# They allow the execution of different code blocks depending on whether a condition evaluates to True or False. 

# Python's main conditional statements include if, elif, and else.

# In[38]:


# if condition statement : -  Code block to execute if condition is True
x = 10
if x > 5:
    print("x is greater than 5")


# In[39]:


# else condition statement : - Code block to execute if condition is False
a = 3
if a > 5:
    print("a is greater than 5")
else:
    print("a is 5 or less")


# In[40]:


# elief condition statement : - It allows you to check multiple conditions. It is used after an if statement and before an else statement.
a = 6
if a > 10:
    print("a is greater than 10")
elif a > 5:
    print("a is greater than 5 but not greater than 10")
else:
    print("a is 5 or less")


# # Q.7) Describe the different types of loops in Python and their use cases with examples

# In Python, loops are used to execute a block of code repeatedly based on certain conditions. 

# There are two loops 
# 1) while loop 
# 2) for loop 

# 1. while loop :- The while loop executes a block of code as long as a given condition is True. It is useful when the number of iterations is not known beforehand and is determined by some condition.

# 1) for Loop:-
# The for loop in Python is used to iterate over a sequence and execute a block of code for each item in the sequence.

# In[41]:


# while loop :- 
count = 10
while count < 20:
    print(count)
    count += 1


# In[42]:


row = 1
while row <= 10:
    col = 1
    while col <= row:
        print("$", end = " ")
        col = col + 1
    print()
    row = row + 1


# In[43]:


# for loops 
for i in range(5):
    for j in range(i + 1):
        print("@", end = " " )
    print()


# # THANK YOU!!

# In[ ]:




