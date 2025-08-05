# Create an empty dictionary called bird
# Add name, color, breed, legs, age to the bird dictionary
# Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
# Get the length of the student dictionary
# Get the value of skills and check the data type, it should be a list
# Modify the skills values by adding one or two skills
# Get the dictionary keys as a list
# Get the dictionary values as a list
# Change the dictionary to a list of tuples using items() method
# Delete one of the items in the dictionary
# Delete one of the dictionaries

birds={"name":"eagle","colour":"black","breed":"snake","legs":2,"age":3}
print(birds)

# Create a student dictionary and add first_name, last_name, gender, age, marital_status, skills, country, city and address as keys for the dictionary
student={"first_name":"akhila","last_name":"devassia","gender":"female","marital_status":"single",
         "skills":["python","c"]}
print(student)
# Get the length of the student dictionary
print(len(student))

# Get the value of skills and check the data type, it should be a list
print(student['skills'])
print(type(student['skills']))

# Modify the skills values by adding one or two skills
student['skills'].extend(["embedded c",'c++'])
print(student)

## Get the dictionary keys as a list
li=list(student.keys())
print(li)
# Get the dictionary values as a list
li=list(student.values())
print(li)

# Change the dictionary to a list of tuples using items() method
lis_items=list(student.items())
print(lis_items)


# Delete one of the items in the dictionary
del student["gender"]
print(student)
# Delete one of the dictionaries
del student