'''Q1) Create list called "even", store all the even numbers, in the range of 1 to 20.'''
even=[]
for i in range(1,21):
    if i%2==0:
        even.append(i)
print(even)


'''Create list called "odd", store all the odd numbers, int the range of 1,20.'''
odd=[]
for i in range(1,21):
    if i%2!=0:
        odd.append(i)
print(odd)


'''Take "even" and "odd" list  from previous solution, merge it in new list called "numbers" and sort it.'''
numbers=even+odd
numbers.sort()
print(numbers)

'''Create a nested list for called "Students" for 5 student, each index store the student information. ex.. ["name",roll,marks].'''
students = [["akhila",1,33],["sandra",2,34],["merita",3,44],["ashwathi",5,66],["aleena",8,56],["aneesh",9,78]]
print(students)

#Write a Python program to find the second largest number in a list.

l=list[0]
list=[1,2,3,4,5]
list.sort()
print(list[-2])

#WAP to print unique element from list.
nums = [4,3,5,6,3,4,6]

num=[4,3,5,6,3,4,6]


#Q7) Given a tuple of numbers, find the max and min elements.
#tup = (11,26,45,23,15,18)

tup = (11,26,45,23,15,18)
print("maximum",max(tup))
print("minimum",min(tup))


#Q8) Retrieve the 'G' from following list using positive indexing
l= [1, 2,'hi',(21, 78, [-2, -4,('Bahubali', 'KGF', 'RRR')])]
print(l[3][2][2][1][1])


#Q9) WAP to retrieve the 'Sweet' string from the following nested list using Positive indexing
L2 = [21, ['Anil', 'Education', [['Java', 'Kova'], ['Programming', 'Sugar', 'Sweet', 'Wheat']]], 7065, 5, 2034, [1, 2]]
print(L2[1][2][1][2])

#Q10) WAP to extract 'Bengaluru' in reverse order using negative indexing from following string
     # s2 = 'Hello I am going to Bengaluru How are you doing?'''

s2 ='Hello I am going to Bengaluru How are you doing?'
print(s2[-19:-29:-1])






