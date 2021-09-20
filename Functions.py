''' Write a program to demonstrate usage of functions, passing list as argument, 
recursion, local and global socpe using in Python.'''

# This Program is made by Prakhar Jain.

#Function defination
def greet(name):
    """
    This function greets to
    the person passed in as
    a parameter
    """
    print("Hello, " + name + ". Good morning!")

#Function call
greet('Paul')


#Return Statement
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""
    if num >= 0:
        return num
    else:
        return -num
print(absolute_value(2))
print(absolute_value(-4))


# Passing a List as an Argument
def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)


#Recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

num = 3
print("The factorial of", num, "is", factorial(num))


# local and global socpe using in Python
x = "global " #This is a global variable

def foo():
    global x
    y = "local" #This is a local variable
    x = x * 2
    print(x)
    print(y)

foo()
