#level 1
# #1.  Area of a circle is calculated as follows: area = π x r x r and perimeter = 2 x π x r.
# #  Write a function that calculates area_of_circle and perimeter_of_circle.
def area_of_circle(r):
    area=3.14*r*r
    print(area)
def area_of_perimeter(r):
    perimeter=2*3.14*r
    print(perimeter)
a=int(input("enter the number"))
area_of_circle(a)
area_of_perimeter(a)
#
# # 2. Write a function called add_all_nums which takes arbitrary number of arguments and
# # # sums all the arguments.
# # # Check if all the list items are number types. If not do give a reasonable feedback.
# #
def add_all_nums(numbers):
    if not isinstance(numbers,list):
        return "only list numbers"
    for i in numbers:
        if not isinstance(i,int):
            return "only int numbers"
    return sum(numbers)
print(add_all_nums([1, 2, 3]))
print(add_all_nums([1, 2, "abcd"]))
print(add_all_nums([]))
print(add_all_nums(("bchd","abcd")))
#
#
# # 3.Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32.
# # Write a function which converts °C to °F, convert_celsius_2_fahrenheit.
#
def convert_celsius_2_fahrenheit(c):
    f=(c*9/5)+32
    print(f)
a=25
print(convert_celsius_2_fahrenheit(a))
#
# # 4.Write a function called check_season,
# # it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    if month in ['december', 'january', 'february']:
        return 'Winter'
    elif month in ['march', 'april', 'may']:
        return 'Spring'
    elif month in ['june', 'july', 'august']:
        return 'Summer'
    elif month in ['september', 'october', 'november']:
        return 'Autumn'
    else:
        return 'Invalid month name'
a=input("enter the month")
print(check_season(a))
#
#  # 7.Declare a function named print_list.
# # It takes a list as a parameter and it prints out each element of the list.
def print_list(num):
    for i in num:
        print(i)
a = [1, 2, 2, 3, 4, 5, 5, 5, 6]
print_list(a)
#
# #8. Declare a function named reverse_list.
# # It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(arr):
    rev=[]
    for i in range(len(arr)-1,-1,-1):
        rev.append(arr[i])
    return rev
print(reverse_list(['a','b','c']))
#
# #9. Declare a function named capitalize_list_items.
# # It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(n):
    rev=[]
    for i in n:
        a=i.capitalize()
        rev.append(a)
    return rev

st=['apple', 'banana', 'cherry']
print(capitalize_list_items(st))

# # # 10)Declare a function named add_item. It takes a list and an item parameters.
# # It returns a list with the item added at the end.
def add_item(item):
    item.append('cherry')
    print(item)
a=['apple','orange']
add_item(a)

# # 11.Declare a function named remove_item. It takes a list and an item parameters.
# # It returns a list with the item removed from it.
def remove_item(item):
    item.remove('Mango')
    print(item)
food_staff=['Potato', 'Tomato', 'Mango', 'Milk']
remove_item(food_staff)

# # #12) Declare a function named sum_of_numbers.
# # # It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(number):
    s = 0
    for i in range(1,number+1):
        s = s + i
    return s
a=int(input("enter the number :"))
out = sum_of_numbers(a)
print(f"Sum of numbers up to {a} are : {out}")
# #
# # # 13.Declare a function named sum_of_odds.
# # # It takes a number parameter and it adds all the odd numbers in that range.
# #
def sum_of_odds(number):
    s=0
    for i in range(1,number+1):
        if i%2 != 0:
            print(i,end=' ')
            s=s+i
    return s
a=int(input("enter the number"))
print(sum_of_odds(a))
#
# # #14 Declare a function named sum_of_even.
# # # It takes a number parameter and it adds all the even numbers in that - range.
def sum_of_even(number):
    s=0
    for i in range(1,number+1):
        if i%2 == 0:
            print(i,end=' ')
            s=s+i
    return s
a=int(input("enter the number"))
print(sum_of_even(a))
#
# #level 2
# # #1. Declare a function named evens_and_odds.
# # # It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds():
    s=0
    s1=0
    for i in range(1,20+1):
        if i%2==0:
            s=s+i

        else:
            s1=s1+i
    print(s)
    print(s1)
evens_and_odds()
#
# # # Call your function factorial,
# # # it takes a whole number as a parameter and it return a factorial of the number
# #
def factorial(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact * i
    return fact
num = int(input("Enter the number :"))
f = factorial(num)
print(f"Factorial of {num} : {f}")
#
# # Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(n):
    if n=='' or n==[] or n=={} or n==() or n is None:
        return True
    else:
        return False

print(is_empty(''))
print(is_empty([]))
print(is_empty({}))
print(is_empty(1))
print(is_empty(None))
#
# # Write different functions which take lists.
# # They should calculate_mean, calculate_median, calculate_mode,
# # # calculate_range, calculate_variance, calculate_std (standard deviation).
# # def calculate_mean(num):
# #     a=sum(num)/len(num)
# #     print(a)
# # a = [1, 2, 2, 3, 4, 5, 5, 5, 6]
# # # calculate_mean(a)

# Write a function called is_prime, which checks if a number is prime.
def is_prime(num):
    co = 0
    for i in range(1,num+1):
        if num%i == 0:
            co+=1
            # print(f"{co}")

    if co == 2 and num!=0:
        print(f"{num} is Prime")

    else:
        print(f"{num} is not Prime")
a=int(input("enter the num"))
is_prime(a)

