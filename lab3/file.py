import keyword
from random import randint
my_text = "Hi there, this is an updated Python script"
my_int = 12
my_float = 2.718
my_list = ["orange", my_int, my_float, "data", my_text]
my_dict = {
    "fruit": "kiwi",
    "number": my_int,
    "message": my_text
}
my_tuple = ("Coding", my_text)
my_set = {"greetings", my_text + "!!", str(my_int)}

print("Text variable:", my_text)
print("Integer:", my_int)
print("Float:", my_float)
print("List:", my_list)
print("Dictionary:", my_dict)
print("Tuple:", my_tuple)
print("Set:", my_set)

#2
print("First constant:", False)
print("Second constant:", None)
print(f"Using a constant inside f-string: {True}")
print("\nList of Python reserved words:")
print(keyword.kwlist)

print("Absolute value of -9.8:", abs(-9.8), f"is equal to {abs(9.8)}", "and comparison:", abs(-9.8) == abs(9.8))
print("Maximum value among 3, 14, 7:", max(3, 14, 7))
print("Minimum value among 3, 14, 7:", min(3, 14, 7))
print("Length of the string 'Programming':", len("Programming"))

fruits = ["mango", "pear", "melon"]
for index, fruit in enumerate(fruits):
    print(f"Fruit at position {index} is {fruit}")

#3


A = randint(0, 1)
print(f"A happened to be {A}" if A else "Looks like A={}".format(A))

#4
A = 0
try:
    print("Trying to compute", 25/A, "?")
except Exception as e:
    print("Caught an error >", e)
finally:
    print("Execution continues regardless!")

#5
def get_name_age(name, age):
    return name, age

#6
with open("example.txt", "w") as f:
    f.write("Hi!\n")
    f.write("This file was generated automatically\n")
    f.write("End of file\n")

#7
with open("example.txt", "r") as f:
    for index, line in enumerate(f):
        print(f"{index} -> {line.strip()}")

#8
my_lambda = lambda first, age: f'Author: {first}, current age: {age:10d} years'

print("Regular function:", get_name_age)
print("Lambda function:", my_lambda)
print("Calling lambda:", my_lambda('Sofia', 555555))
print(my_lambda(*get_name_age("Bob", 33)))
