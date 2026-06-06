# Write a Python program that filters out even numbers using the filter() function. 

def even(n):
    return n%2==0
numbers=[1,2,3,4,5,6,7,8,9,10]
iseven=list(filter(even,numbers))
print(numbers)
print(iseven)