#!/usr/bin/env python
# coding: utf-8

# # Q.1) Discuss string slicing and provide examples.

# In String, Slicing is the Technique in programming that allows you to exract substring from string using indices.

# In[ ]:


#syntax of slicing
string[start:end:step]


# 1) start: The index at which to start the slice. 
# 2) end: The index at which to end the slice. 
# 3) step: The interval between characters in the slice.

# In[11]:


#Example 
String = "PW Skills For Data Analyst"
Substring = String[1:12] # slicing from 1 to 11
print(Substring)


# In[7]:


text = "Hello, World!"

# Slice from index 7 to 12
substring = text[7:13]

print(substring) 



# In[14]:


String = "PW Skills For Data Analyst"
#slicing from start to seven elements
Start_to_seven = String[:8]
print(Start_to_seven)


# In[17]:


#Slice every second character from index 0 to 15
String = "PW Skills For Data Analyst"
Sub_string = String[0:16:2]
print(Sub_string)


# # Q.2) Eplain the key Features of lists in Python
# 

# Lists in Python are one of the most versatile and widely used data structures. They provide a way to store collections of items

# # 1)  Ordered Collection

# Lists maintain the order of elements as they are inserted. 

# In[20]:


#ordered collection
PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
PW_Classes


# # 2). Mutable

# Lists are mutable, It means you can change, edit, remove, modify etc elememnts in the list

# In[35]:


#Mutable, Adding the elements
PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
PW_Classes.append("Competetive")


# In[36]:


PW_Classes


# In[37]:


#Remove the Elements
PW_Classes
PW_Classes.remove("Competetive")
print(PW_Classes)


# # 3). Indexed
# 

# Each element in a list has an index, which is an integer representing its position in the list.

# In[43]:


PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
PW_Classes[4]


# In[44]:


PW_Classes[1:5]


# # 4) Dynamic Size

# Lists automatically adjust their size as elements are added or removed

# In[46]:


#Example
PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
PW_Classes.remove("Skills")
print(PW_Classes)


# # 5) Slicing
# 

# You can access a subset of the list using slicing syntax 

# In[47]:


#Example
PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
PW_Classes[1:5]


# # 6) Iteration

# You can loop through the elements of a list using loops.

# In[51]:


PW_Classes = ["GATE", "Skills", "NEET", "JEE", "SSC", "UPSC"]
for item in PW_Classes:
    print(item)


# In[50]:


a = [1, 2, 3]
for item in a:
    print(item)


# # 7) List Comprehensions

#  A concise way to create lists using a single line of code.

# In[52]:


squares = [x**2 for x in range(5)]
print(squares)


# In[62]:


cubes = [x**3 for x in range(6)]
print(cubes)


# # 8) Supports Various Data Types

# You can add any type of data in list of python 

# In[63]:


#example
My_list = ["Movie", 1, 56, 5.3, True, "etc..."]


# In[64]:


My_list


# # Q.3) Describe how to access, modify, and delete elements in a list with examples

# We can access, modify, and delete elements in a Python list, there is explaination with examples

# # Accessing Elements:- 
# 

# To access elements in a list, you use indexing. Python lists are zero-indexed, meaning the first element has an index of 0.

# In[1]:


#Accessing the elements from fruits 
Fruits = ["Banana", "apple", "Pineapple", "watermelon", "Orange" ]
Fruits


# In[4]:


# Accessing
Access = Fruits[1:3]
Access


# In[8]:


# deleting
# we can delete elements using the del statement, the remove() method
# use del
del Fruits[2], # we delete 2nd element
Fruits


# In[14]:


# Using remove method
Fruits = ["Banana", "apple", "Pineapple", "watermelon", "Orange" ]
Fruits


# In[19]:


Fruits.remove("apple")
Fruits


# # Q.4) Compare and contrast tuples and lists with examples

# 
# 1) List:- A mutable collection of items that can be modified after creation.
# 2) Tuple:- An immutable collection of items that cannot be modified once created.

# List are mutable and Tuples are immutable

# In[21]:


# Example of Tuple
Tuple = (1,2,3,4,5)
Tuple


# In[22]:


# Example of list 
List = [1,2,3,4,5]
List 


# In[27]:


# We can modify list but cant Tuple
List.append(6)
List


# Use Cases
# 1) List:- Best used when you need a collection of items that may change over time, such as in a dynamic dataset.
# 2) Tuple:- Best used for fixed collections of items, such as coordinates, RGB color values, or returning multiple values from a function.

# # Q.5) Describe the key features of sets and provide examples of their use

# Key Features of Sets
# 1) Unordered: Sets do not maintain any order for their elements. Each time you create a set, the order of the elements may change.
# 
# 2) Unique Elements: Sets automatically eliminate duplicate entries. Each element in a set is unique.
# 
# 3) Mutable: Sets can be modified after creation. You can add or remove elements.
# 
# 4) Dynamic Size: Sets can grow or shrink in size as elements are added or removed.
# 
# 5) Support for Mathematical Operations: Sets support operations like union, intersection, difference, and symmetric difference.

# In[28]:


# Using curly braces
my_set = {1, 2, 3, 4}

print(my_set)         


# In[29]:


# Using the set() constructor
set1 = set([3, 4, 5, 6])
set1


# In[30]:


# Adding an element
my_set.add(5)
print(my_set)  


# In[31]:


# Removing an element
my_set.remove(3)
print(my_set)  # Output: {1, 2, 4, 5}


# In[34]:


# remove duplicate value or elements
duplicate_set = {1, 2, 2, 3, 4, 4}
print(duplicate_set)  


# # Set Operations

# Sets support various mathematical operations:
# 
# 1) Union: Combines elements from both sets.
# 2) Intersection: Finds common elements between sets.
# 3) Difference: Finds elements in one set that are not in another.
# 4) Symmetric Difference: Finds elements in either set, but not in both.
# 

# In[35]:


set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Union
print(set_a | set_b)       


# In[36]:


# Intersection
print(set_a & set_b)                   


# In[37]:


# Difference
print(set_a - set_b)             


# In[38]:


# Symmetric Difference
print(set_a ^ set_b)  


# Use Cases
# 1) Remove Duplicates = You can convert a list to a set to eliminate duplicates.
# 2) Mathematical Operations: Useful in problems involving group memberships or data analysis. 

# In[39]:


# Remove duppliocate
List = [1,2,3,3,4,4,5,5,5,4,9,8,2,6,7,4,5,8]
List


# In[41]:


unique_items = set(List)
unique_items


# # Q. 6) Descuss the use cases of tuples and sets in Python programming

# Use Cases for Tuples
# 1) Immutable Data:
# 
# a) Fixed Collections: Use tuples to represent collections of items that should not change, such as coordinates (latitude, longitude) or RGB color values.
# b) Function Returns: When a function needs to return multiple values, tuples provide a simple way to group them together.

# In[42]:


def get_coordinates():
    return (34.0522, -118.2437)  

real_Coordinates = get_coordinates()
print(real_Coordinates)  


# 2) Data Integrity:
# 
# a) Prevent Modification: Since tuples are immutable, they can help ensure that data remains unchanged, which is useful for protecting critical data.
# 

# In[45]:


location_data = {
    (34.0522, -118.2437): "Los Angeles",
    (40.7128, -74.0060): "New York"
}
location_data


# In[47]:


# Heterogeneous data 
data = ("Aaksh", 23, 2.5)
data


# Sets
# Characteristics:
# 
# Unordered: Sets do not maintain any order, meaning the items cannot be accessed by index.
# Mutable: Sets can be modified after creation—elements can be added or removed.
# Unique Elements: Sets automatically handle duplicates, ensuring that each element is unique

# # Q.7) Describe how to add, modify and delete items in a dictionary with examples

# In[48]:


# Adding the elements
my_dict = {'a': 1, 'b': 2}

my_dict['c'] = 3

print("After adding:", my_dict)


# In[49]:


# Modifying the existing elements of dictionary
my_dict['b'] = 5

print("After modifying:", my_dict)


# In[50]:


# Deleting Items 
del my_dict['a']

print("After deleting 'a':", my_dict)


# # Q. 8) Discuss the importance of dictionary keys being immutable and provide examples

# 
# Importance of Immutable Dictionary Keys
# 
# 1) Consistency and Stability:- Immutable keys ensure that the hash value of the key does not change over time. This is crucial for maintaining the integrity of the dictionary. If keys were mutable, their hash values could change, leading to unpredictable behavior when trying to access values.
# 
# 
# 2) Hashing Mechanism:- Dictionaries in many programming languages (like Python) use a hashing mechanism to quickly retrieve values based on keys. If a key is mutable and its state changes, it can lead to collisions or the key becoming inaccessible, resulting in lost data.
# 
# 
# 3) Avoiding Bugs:- Mutable keys can introduce subtle bugs in code, especially in concurrent environments where multiple threads might be accessing or modifying keys. Immutability prevents such scenarios, leading to more reliable and predictable code.
# 

# In[ ]:




