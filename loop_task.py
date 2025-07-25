#Iterate 0 to 10 using for loop,
for i in range(0,11):
    print(i,end=" ")

#do the same using while loop.
i = 0
while (i <= 10):
    print(i, end=" ")
    i = i + 1

#Iterate 10 to 0 using for loop,
for i in range(10, -1, -1):
    print(i, end=" ")
# do the same using while loop.
i = 10
while (i >= 0):
    print(i,end=" ")
    i = i - 1

#Write a loop that makes seven calls to print(), so we get on the output the following triangle:
rows = 8
for i in range(rows):
    hashes = '# ' * rows
    print(hashes)

#Use nested loops to create the following:
rows = 7
for i in range(rows):
    space = ' ' * (rows - i - 1)
    hashes = '#' * (2 * i + 1)
    print(space + hashes)

#Print the following pattern using loops
for i in range(0, 11):
    print(f"{i}*{i}={i * i}")

#Iterate through the list, ['Python', 'Numpy','Pandas','Scikit', 'Pytorch'] using a for loop and print out the items.
list = ["Python", "Numpy", "Pandas", "Scikit", "Pytorch"]
for i in list:
    print(i,end=" ")
print()

#Use for loop to iterate from 0 to 100 and print only even numbers
for i in range(0, 100):
    if i % 2 == 0:
        print(i,end=" ")
print()

# Use for loop to iterate from 0 to 100 and print only odd numbers
for i in range(0, 101):
    if i % 2 != 0:
        print(i,end=" ")
print()
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(0, 101):
    sum = sum + i

print(sum)

#Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum=0
sum1=0
for i in range(0,101):
    if i%2==0:
        sum=sum+i
    else:
        sum1=sum1+i

print("even:",sum)
print("odd:",sum1)
