# Q1) Create a dictionary named student_info with the following keys:          student_name, age, roll_no, class, section, percentage, college_name.
#           a) Print all the keys and values from the dictionary.
#           b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
#           c) Delete the section key from the dictionary.
#           d) Use a loop to print all key-value pairs in the dictionary in the format:
# Key --> Value
#           e) Check if the key 'college_name' exists in the dictionary or not.
#a) Print all thekeys and values from the dictionary.
student_info={ "student_name":"Ramya",
               "age":15,
               "roll_no":1,
               "class":"X",
               "section":'A',
               "percentage":89,
               "college_name":"VJEC",}

print(student_info)
#b) Add a new key-value pair: 'email': 'student@example.com' to the dictionary.
student_info.update({"email":"ramya@gmail.com"})

#c) Delete the section key from the dictionary.
print(student_info)
student_info.pop("section")
# del student_info["section"]
print(student_info)
#d) Use a loop to print all key-value pairs in the dictionary in the format:
# Key --> Value
for x,y in student_info.items():
    print(x,"-->",y)
# e) Check if the key 'college_name' exists in the dictionary or not.
if "college_name" in student_info:
    print("yes, college name is available")
else:
    print("no,college name is not available")


# python_students = {"Alice", "Bob", "Charlie", "David"}
# java_students = {"Bob", "Eve", "Frank", "David"}
# cpp_students = {"Charlie", "George", "Eve", "Henry"}
# Find students who are enrolled in all three courses.
# Find students who are enrolled in only Python course.
# Find students who are enrolled in both Python and Java.
# Find students who are enrolled in either Python or Java but not both.
# Find the list of all unique students enrolled in any course.
# Find students who are in Java or C++, but not in Python.
# Check if all Python students are also Java students.
# Add a new student "Jones" to the Python set.
# Remove "Frank" from the Java set.
# Clear the cpp_students set.

python_students = {"Alice", "Bob", "Charlie", "David"}
java_students = {"Bob", "Eve", "Frank", "David"}
cpp_students = {"Charlie", "George", "Eve", "Henry"}

# Find students who are enrolled in all three courses.
students=python_students&java_students&cpp_students
print(students)

#Find students who are enrolled in only Python course.
students=python_students-java_students-cpp_students
print(students)

#Find students who are enrolled in both Python and Java.

students=python_students&java_students
print(students)

#Find students who are enrolled in either Python or Java but not both.
students=python_students^java_students
print(students)
#Find the list of all unique students enrolled in any course.

students=python_students|cpp_students|java_students
print(students)

#Find students who are in Java or C++, but not in Python.

students=((cpp_students|java_students)-python_students)
print(students)

# Check if all Python students are also Java students.
students=python_students.issubset(java_students)
print(students)

#Add a new student "Jones" to the Python set.

python_students.add("Jones")
print(python_students)

#Remove "Frank" from the Java set.
java_students.remove("Frank")
print(java_students)

#Clear the cpp_students set.
cpp_students.clear()
print(cpp_students)

