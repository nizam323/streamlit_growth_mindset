
# # functons
# def greet(name):
#     return "hello "+ name
# result = greet("test")
# print(result)

# # loops
# for i in range(5):
#     i += 1
#     print(i)
# i = 0
# while i < 5:
#     print("before increment",i)
#     i += 1 
#     print("after increment",i)

## conditions
# age = 25
# if age > 18:
#     print("older than 18")
# elif age < 18:
#     print("younger than 18")
# else:
#     print("else message")

## variables and data types
# name = "John"  # String
# age = 25       # Integer
# is_student = True  # Boolean (Note: 'True' starts with an uppercase 'T')
# fruits = ["apple", "banana", "cherry"]  # List (same as an array)
# person = { "name": "Alice", "age": 30 }  # Dictionary (like an object)

## f string
# name = "test"
# print(f"hello {name}")

## arrow function
# add = lambda num1, num2: num1 + num2 
# print(add(5,10))

## ternary operator
# age = 18
# result = "adult" if age >= 18 else "minor"
# print(result)

## lists (like arrays in js)
# users = ["test1","test2","test3",]
# print(users)
# print(users[1])
# users.append("test4")
# print(users)

## Dictionaries (Like Objects in JS)
# obj = {"name":"test","age":33}
# obj["dd"] = "d"
# print(obj)

## list comprehension ( .map() ) in python

# users = [
#     {
#         "name":"test1",
#         "age":22
#     },
#     {
#         "name":"test2",
#         "age":223
#     },
#     {
#         "name":"test3",
#         "age":2
#     },
#     {
#         "name":"test4",
#         "age":25
#     },
# ]
# print("users",users)
# [ print(i["name"],i["age"]) for i in users ]

## import modules
# import math  # Imports entire module
# from math import sqrt  # Imports only 'sqrt' function

## Logical Operations 
# x = 10
# y = 5
# print(x > 5 and y < 10)  # True
# print(x > 5 or y > 10)   # True
# print(not x > 5)       # False