# Write a Python program that uses reduce() to find the product of a list of numbers.

from functools import reduce
def multiply(x,y):
    return x*y
numbers=[1,2,3,4]
product=reduce(multiply,numbers)
print(numbers)
print(product)