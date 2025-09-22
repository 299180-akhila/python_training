# Q1) Write a Python program to implement the following:
# Class: Person
# Attributes: Age, Name, Gender, Address
# Methods:
# Constructor to initialize attributes
# Display() to print details

class Person:
    def __init__(self,name,age,gender,address):
        self.name=name
        self.age=age
        self.gender=gender
        self.address=address
    def display(self):
        print(self.name,self.age,self.gender,self.address)
obj1=Person("ashwathi",20,"female","kerala")
obj1.display()

# Class: Student (inherits from Person)
# Attributes: Roll, Marks, College
# Methods:
# Constructor to initialize both Person and Student attributes
# Display() to print all details

class Student(Person):
    def __init__(self,Roll,Marks,College):
        self.Roll=2
        self.Marks=40
        self.College="vjec"
    def display(self):
        print(self.Roll,self.Marks,self.College)
obj1=Student(2,40,"VJEC")
obj1.display()

# Class: Intern (inherits from Person)
# Attributes: InternId, Company, Duration
# Methods:
# Constructor to initialize both Person and Intern attributes
# Display() to print all details

class Intern(Person):
    def __init__(self,InternId,Company,Duration):
        self.InternId=InternId
        self.Company=Company
        self.Duration=Duration
    def display(self):
         print(self.InternId,self.Company,self.Duration)
obj2=Intern(34,"Microsoft",1234)
obj2.display()


# Class: Employee (inherits from Student and Intern)
# Represents a diamond inheritance problem.
# Attributes: EmpId, Salary
# Methods:
# Constructor to initialize attributes of all parent classes (Person, Student, Intern) and Employee.
# Display() to print complete details (Person + Student + Intern + Employee).
class Employee(Student,Intern):
    def __init__(self,name,age,gender,address,Roll,Marks,College,InternId,Company,Duration,EmpId,Salary,):
        self.InternId = InternId
        self.Company = Company
        self.Duration = Duration
        self.EmpId = EmpId
        self.Salary = Salary
    def display(self):
        print(self.InternId,self.Company,self.Duration,self.EmpId,self.Salary)
obj1=Employee("akhila",24,"female","kerla",3,67,"vjec",123,"Microsoft",12345,23,300000)
obj1.display()





