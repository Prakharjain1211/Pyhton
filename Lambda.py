''' Write at least 10-15  problem codes   to demonstrate 
usage of Lambda functions in Python (with use of map, filter , reduce etc.)'''

# This Program is made by Prakhar Jain.

# Program to show the use of lambda functions
double = lambda x: x * 2
print(double(5))


# Use with filter()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(filter(lambda x: (x%2 == 0) , my_list))
print(new_list)


# Use with map()
my_list = [1, 5, 4, 6, 8, 11, 3, 12]
new_list = list(map(lambda x: x * 2 , my_list))
print(new_list)


# Use with reduce
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)
