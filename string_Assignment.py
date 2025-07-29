# Coding Questions
# Write a Python program that takes a string and removes all vowels.
# Given a string, write a program to count the frequency of each character.
# Write a Python program to check if two given strings are anagrams of each other
# Write code to reverse the order of words in a sentence, without using built-in reverse functions
# Write a Python program to find the longest substring without repeating characters.
# Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
# Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
# with out using Title()

# Write a Python program that takes a string and removes all vowels.
s=input("enter the string")
vowels="aeiouAEIOU"
result=""
for ch in s:
    if ch not in vowels:
        result+=ch
print(result)

# Given a string, write a program to count the frequency of each character.
s=input("enter the string")
fre={}
for ch in s:
    if ch in fre:
     fre[ch]=fre[ch]+1
    else:
        fre[ch]=1
print(fre)

#Write a Python program to check if two given strings are anagrams of each other

# Write code to reverse the order of words in a sentence, without using built-in reverse functions
s='where are you'
s1=s.split()
print(s1)
rever=' '
i=len(s1)-1
while i>=0:
    rever=rever+s1[i]+' '
    i=i-1
print(rever)

# Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
str= "malayalam"
if str == str[::-1]:
    print("palindrome")
else:
    print("not a palindrome")

#Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
# with out using Title()
# with out using Title()
a='where are you'
b=' '
for i in range(0,len(a)):
    if i==0 or a[i-1]==' ' :
        =b+a[i].upper()
    else:
        b = b + a[i]
print(b)

