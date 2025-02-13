# course outline

# introduction
# python is a high level programming language that is used for web development, data science, machine learning, artificial intelligence, automation, etc.
# python is a general purpose programming language
# python is easy to learn and use
# python is free and open source
# python is interpreted language
# python is object oriented programming language
# python is cross platform language
# python is interactive language
# python is portable language
# python is dynamic language
# name = "wale"
# age = 18
# print(2 + 2)
# installation
# vscode, pycharm, jupyter notebook, google colab, etc.

# input and output

# print is a way of displaying data on the screen, printing data to the console, writing data to a file, etc.
# print(2 + 2)
# print('wale')
# print("2 + 2 = ", 2 + 2)

# input is a way of getting data from the user
# input("Enter your name: ")

# variables is a way of storing data in memory
# age = 18
# print(age)

# username = input("Enter your username: ")
# print("welcome", username)

# variable rules
# - should not start with numbers eg. 2numbers = 2 + 4
# - should not contain special characters eg. @, #, $, %, ^, &, *, (, ), etc. except underscore _ eg _name = "wale"
# - should not be a reserved keyword eg. if, else, for, while, etc.
# - should not contain spaces eg. first name = "wale", should be first_name = "wale"
# - should be a descriptive name eg. name, username, user_id, etc. total_profit= 500

#list of reserved words in python
# class 
# if 
# else 
# for 
# while 
# yield 
# break 
# continue 
# pass 
# return 
# try 
# except 
# raise 
# import 
# from 
# as 
# global 
# nonlocal 
# lambda 
# with 
# async 
# await 
# class 
# def 
# del 
# in 
# is 
# not 
# or 
# and 
# True 
# False 
# None

# data types is a way of classifying data in python, there are different types of data in python
# - strings is a sequence of characters eg. "wale", "2 + 2"
# it is denoted by single quotes or double quotes or triple quotes eg. 'wale', "wale", '''wale''', """wale"""
# it is immutable
# message = "Dear Sir,\nI hereby apply for the position of a devops engineer in your company.\nI have 5 years experience in devops.\nI have experience in AWS, GCP, Azure, etc.\nI have experience in Jenkins, Docker, Kubernetes, etc.\nThank you"
# # print(message)
# new_message = """Dear Sir,
# # I hereby apply for the position of a devops engineer in your company.
# # I have 5 years experience in devops.
# # I have experience in AWS, GCP, Azure, etc.
# # I have experience in Jenkins, Docker, Kubernetes, etc.
# # Thank you"""

# print(new_message)

address = "70c Allen Avenue, Ikeja, Lagos"
# len is a function that returns the length of a string
print(len(address))

# indexing is a way of accessing a character in a string
print(address[4])
print(address[-1])

# slicing is a way of accessing a range of characters in a string
print(address[4:9])
print(address[25:30])
print(address[-5:])
print(address[:30])

# steps is a way of accessing characters in a string with a step

numbers = "123456789"
print(numbers[0:9:2])
print(numbers[1:9:2])
print(numbers[-2:-9:-1])
print(numbers[7:0:-1])

data = "A:1 B:2 C:3 D:4 E:5"
print(data[2:19:4])
# print(len(data))

words = "   welcome to python class   "
# string methods
# capitalize - capitalizes the first character of a string
print(words.capitalize())

# upper - converts all characters in a string to uppercase
print(words.upper())

# title - capitalizes the first character of each word in a string
print(words.title())

# lower - converts all characters in a string to lowercase
print(words.lower())

# count - counts the number of occurrences of a character in a string
print(words.count("w"))

# find - returns the index of the first occurrence of a character in a string
print(words.find("python"))

# replace - replaces a character in a string with another character
print(words.replace("python", "devops"))
words = words.replace("python", "devops")
print(words)

# split - splits a string into a list of words
print(words.split())
print(words)
record = words.split()
print(record)

# join - joins a list of words into a string
print(" ".join(record))

# strip - removes leading and trailing spaces in a string
print(words.strip())

# lstrip - removes leading spaces in a string
print(words.lstrip())

# rstrip - removes trailing spaces in a string
# print(words.rstrip())
# info = "123!"
# # isdigit - checks if a string is a digit
# print(info.isdigit())

# # # isalpha - checks if a string is an alphabet
# print(info.isalpha())

# # isalnum - checks if a string is an alphanumeric
# print(info.isalnum())


# Assignment
# 1. Write a program that takes two numbers as input from the user and prints the sum of the two numbers
# eg. if 2 and 8 are the two numbers, it should return 10
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# print("The sum of the two numbers is", num1 + num2)

# 2. Write a Python program to reverse a given string.
# Example:
# Input: "hello"
# Output: "olleh"
# word = "hello"
# print(word[::-1])

# 3. Write a Python program to count the number of words in a given string.
# Example:
# Input: "Python is awesome"
# Output: 3
sample = "Python is awesome i believe you agree with me"
print(len(sample.split()))

# 4. Given:
total_money = 1000
quantity = 3
price = 450
# Use the variables above to print out the following output. 
# I have 1000 dollars, so I can buy 3 football for 450 dollars.
print("I have", total_money, "dollars, so I can buy", quantity, "football for", price, "dollars.")
print(f"I have {total_money} dollars, so I can buy {quantity} football for {price} dollars.")

# 5. Write a Python program to convert a string into a URL-friendly slug (lowercase, replace spaces with hyphens, remove special characters).
# Example:
# Input: "My First Blog Post!"
# Output: "my-first-blog-post"
# blog = "My First Blog Post!"
# blog = blog.lower()
# blog = blog.replace(" ", "-")
# blog = blog.replace("!", "")
# print(blog)

# blog = "-".join(blog.lower().split())
# print(blog.replace("!", ""))

# - lists - a list is a collection of items in a particular order eg. [1, 2, 3, 4, 5] 
# it is denoted by square brackets []
# it is mutable - it can be changed
# in list indexing is word by word - starting from index 0
# names = ["wale", "john", "jane", "doe"] 
# numbers = [1, 2, 3, 4, 5]

# # indexing a list
# print(names[2])

# # slicing a list 
# print(names[1:3])

# # list methods
# # append - adds an item to the end of a list 
# names.append("mary")
# print(names)

# # insert - inserts an item at a specified index in a list
# names.insert(1, "james")
# print(names)

# # pop -  the last item in a list if no index is specified
# names.pop()
# print(names)

# # pop removes an item from a list at a specified index
# names.pop(2)
# print(names)

# # remove - removes an item from a list by value
# names.remove("wale")
# print(names)

# # clear - removes all items from a list
# # names.clear()
# # print(names)

# names = ["wale", "john", "jane", "doe"] 
# numbers = [1, 2, 3, 4, 5] 

# # copy - copies a list
# backup = names.copy()
# print(backup)

# # reverse - reverses the order of a list
# names.reverse()
# print(names)

# # sort - sorts a list in ascending order
# names.sort()
# print(names)

# # extend - adds all the items of a list to the end of another list
# names.extend(numbers)
# print(names)

# # nested lists - lists within lists
# staff = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# print(staff[1][1])
# print(staff[2][0:2])
# print(staff[0][1:3])

# # - dictionary data type - a dictionary is a collection of key-value pairs 
# # it is denoted by curly braces {}
# # it is mutable - it can be changed
# # in dictionary indexing is by key 
# # key should be unique 
# record = {"name": "wale","age": 18}
# print(record["age"])

# employees = [ {"name": "wale","age": 18}, 
#              {"name": "mary","age": 25}, 
#              {"name": "john","age": 28}]
# print(employees[1]["name"])

# movies = { "page": 1, "results": [{"adult": 
# False,"backdrop_path": "/b85bJfrTOSJ7M5Ox0yp4lxIxdG1.jpg", 
# "genre_ids": [28, 878, 35, 10751 ],
# "id": 939243,"original_language": "en","title": "Sonic the Hedgehog 3", }]}

# print(movies["results"][0]["title"])

# # dictionary methods
# staff = {"name": "wale","age": 18}

# # get - returns the value of a key in a dictionary
# print(staff.get("name"))

# # keys - returns a list of all the keys in a dictionary
# print(staff.keys())

# # values - returns a list of all the values in a dictionary
# print(staff.values())

# # items - returns a list of all the key-value pairs in a dictionary
# print(staff.items())

# # update - updates the value of a key in a dictionary
# staff.update({"name": "john"})
# print(staff) 

# # adding a new key-value pair to a dictionary
# staff["email"] = "wale@gmail.com"
# print(staff)

# # popitem - removes the last key-value pair in a dictionary
# staff.popitem()
# print(staff)

# # pop - removes a key-value pair from a dictionary by key
# staff.pop("name")
# print(staff) 

# # - tuple data types - a tuple is a collection of items in a particular order eg. (1, 2, 3, 4, 5)
# # it is denoted by parentheses ()
# # it is immutable - it can not be changed 
# days = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday")
# print(days[1])

# # - numbers data types - numbers are used to store numeric values eg. 2,18, 50.4, 100, etc.
# # there are different types of numbers in python
# # - int - integers eg. 2, 18, 100, etc.
# # - float - floating point numbers eg. 50.4, 100.5, etc.

# salary = 50009.5

# # __abs__ - returns the absolute value of a number
# print(salary.__abs__())

# # ceil - returns the smallest integer greater than or equal to a number
# print(salary.__ceil__())

# # floor - returns the largest integer less than or equal to a number
# print(salary.__floor__())

# # add - adds two numbers
# print(salary.__add__(500))

# # - boolean data types - boolean are used to store True or False values
# is_admin = True
# # print(is_admin == 1)

# # - set data types - a set is a collection of items in a particular order eg. {1, 2, 3, 4, 5}
# # it is denoted by curly braces {}
# # it is mutable - it can be changed
# # it does not allow duplicate items 

# x = {1, 2, 3, 4, 5}
# y = {4, 5, 6, 7, 8}
# z = {1,1,1,1,1,2,2,2}
# print(z)

# # union - returns a new set with all items from both sets
# print(x.union(y))

# # intersection - returns a new set with all items that are common to both sets
# print(x.intersection(y))

# # difference - returns a new set with all items that are in the first set but not in the second set
# print(x.difference(y))

# # symmetric_difference - returns a new set with all items that are in either of the sets but not in both sets
# print(x.symmetric_difference(y))

# info = [1,1,1,1,2,2,2,2,3,3,]
# print(set(info))

# # - None - a special data type that represents the absence of a value 
# balance = None

# # operators - operators are used to perform operations on data types
# # - 1. arithmetic operators - used to perform mathematical operations eg. +, -, *, /, %, **, //
# print(2 + 2)
# print(2 - 2)
# print(2 * 2)
# print(2 / 2)
# print(3 % 2) # modulus - returns the remainder of a division
# print(2 ** 2) # exponentiation - returns the result of raising a number to a power
# print(5 // 2) # floor division - returns the result of dividing two numbers and rounds the result to the nearest integer

# # - 2. comparison operators - used to compare two values eg. ==, !=, >, <, >=, <= 
# print(2 == 2) # equal to
# print(2 != 2) # not equal to
# print(3 > 2)
# print(2 < 3)
# print(2 >= 2)
# print(2 <= 2)

# # - 3. logical operators - used to combine conditional statements eg. and, or, not 
# print(5 > 4 or 3 < 2)
# print(5 > 4 and 3 < 2)
# print(not(4 > 3))  

# # assignment operators - used to assign a value to a variable eg. =, +=, -=, *=, /=, %=, **=, //=
# x = 5
# y = 2
# x += y # x = x + y
# print(x)

# x -= y   #x = x - y
# print(x)

#  control flow - control flow is the order in which the computer executes statements in a script
# age = int(input("Enter your age: "))
# if age >= 18: 
#     print("You can vote")
# else:
#     print("Not eligible to vote")

# num = 0
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# elif num == 0:
#     print("Zero")
# else:
#     print("Invalid number")
    
#  loops - a loop is a sequence of instructions that is repeated until a certain condition is met
# while loop - a while loop is used to execute a block of code repeatedly as long as a condition is true 
# while loop (initial value, condition, increment/decrement) 

# number = 1 
# while number <= 10:
#     print(number)
#     number += 1

# number = 2
# while number <= 10:
#     print(number)
#     number += 2

# for loop - a for loop is used to iterate over a sequence eg. list, tuple, dictionary, set, etc. 
# numbers = [1, 2, 3, 4, 5] 
# for i in numbers:  
#     print(i)

# numbers = [1, 2, 3, 4, 5]
# go through the numbers 
# check of the ones without remainder when divided by 2
# print the ones that meet the condition
# for i in range(1,11): 
#     if i % 2 == 0:
#         print(i)

# for i in range(2,11,2): 
#     print(i)  

# number = int(input("Enter a number: "))
# for i in range(1,13):
#     print(f"{number} x {i} = {number * i}")

# Assignment

# 1. 
student_score = [1,2,3,[4,5,[6,7]]]

# in the information above, change 7 to 8
student_score[3][2][1] = 8
print(student_score)
# 2. print out tech365 from the record below

# 
record ={'k1':[{'nest_key':['this is deep',['tech365']]}]}
print(record['k1'][0]['nest_key'][1][0])

# 3. Print out python from the info below

# 
info = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}
print(info['k1'][2]['k2'][1]['tough'][2][0])

# 4. 
message = "Welcome to training"

# Add python to the message above to read  "welcome to python training"
words=(message.lower()).split()
words.insert(2,'python')
new_message = " ".join(words)
print(new_message)

# 5. Write a program that prints the integers from 1 to 100. But for multiples of three print "Fizz" instead of the number, and the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBizz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)
# 6. create a program that takes a score and shows the grade based on the score

# eg.
# 90 - 100 ("Grade A")
# 70 - 89 ("Grade B")
# 50 - 69 ("Grade c")
# 30 - 49 ("Grade D")
# 0 - 29 ("Grade F")

# score = int(input("Enter grade"))
# if score >= 90 and score <= 100:
#     print("Grade A")
# elif score >= 70:
#     print("Grade B")
# elif score >= 50:
#     print("Grade c")
# elif score >= 30:
#     print("Grade D")
# elif score >= 0:
#     print("Grade F")
# else:
#     print("Invalid score")

# 7. 
record = "this is the time to attend python training"
for i in record.split():
    if i[0] == 't':
        print(i)

# bring out the words that start from 't'

# 8. Write a program that counts the number of vowels in a string.
# vowels = "aeiou"
# count = 0
# sentence = input("Enter a sentence: ") # life is not hard
# for i in sentence:
#     if i in vowels:
#         count+= 1
# print(f'we have {count} vowels')
        

# 9. Write a program that check if a string is a palindrome. Palindrome are words that have the same spelling when spelt backwards 
# word = input("Enter a word")
# if word == word[::-1]:
#     print("It is palindrone")
# else:
#     print("It is not")

# 10. Write a program that returns only the last 4 digits of the numbers entered by the user.
# Eg.
# Input 123456789
# Output #####6789

# data = input("Enter your ATM Card 11 digits: ")
# print(((len(data)) - 4) * '#' + data[-4:])
    
# functions - is a way of reusing a block of code

# examples of inbuilt function
# range()
# input()
# split()

# user defined function using def
# def add_two_numbers():
#     return 2 + 5

# add_two_numbers()
# print(add_two_numbers())
# print(add_two_numbers())
# print(add_two_numbers())

# function parameter - allow users to supply argument
# def add_numbers(x,y):
#     print(x + y)

# add_numbers(3,2)
# add_numbers(5,9)
# add_numbers(1,4)

# anonymous function - function without a name eg. lambda
# when you want single line of code
# use the function and dispose it
# lambda x,y: x*y

# higher order function - when you pass a function as parameter inside another function
# map - same number of items that goes in comes out
print(list(map(lambda x: x * 5, range(1,6))))

# filter - when number of items items may not be the number of items that comes out based on certain condition
print(list(filter(lambda x: x % 2 == 0, range(1,11))))

# reduce - when you are returning a single value
sum = 0
for i in range(1,11):
    sum += i 
print(sum)

from functools import reduce
print(reduce(lambda x,y:x+y, range(1,11)))

# write a function that removes duplicate from the string entered
# info = input('enter some strings')
# def remove_duplicates(x):
#     return set(x)
# print(remove_duplicates(info))

def remove_duplicate(x):
    basket =[]
    for i in x:
        if i not in basket:
            basket.append(i)
    print(" ".join(basket))
    
# remove_duplicate(info)
remove_duplicate('1515151515151533331515151')
remove_duplicate('45363536252')

# students = [
#     {"name":"Tokunbo", "score":90},
#     {"name":"Wale", "score":59},
#     {"name":"Mary", "score":40},
#     {"name":"Chuks", "score":85},
# ]


# modules - separating code into different files and importing them 
# import calculator as chuks
# chuks.add_it(4,4)
# chuks.sub_it(4,3)

# packages - combination of several modules

# os module - is used to work with operating system related task
import os
# os.mkdir("tech365")
# os.rmdir('tech365')
# print(os.path)
# print(os.getcwd())
# os.chdir('..')
# print(os.getcwd())
# print(os.listdir())
# os.mkdir('tech365')
# os.rename('tech365', 'wale')

# working with files

# writing into a file
# file = open('wale.txt','w')
# file.write('life is not hard')

# reading a file
# file = open('wale.txt', 'r')
# print(file.read())

#appending into a file
# file = open('wale.txt','a')
# file.write('\nPython is easy')

# exception handling - is a way of handling possible error
# try:
#     print(5/0)
# except:
#     print("Sorry, you cant divide by 0")