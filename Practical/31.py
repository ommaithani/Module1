# Write a Python program to apply the map() function to square a list of numbers. 

def square(n):
    return n*n
numbers=[1,2,3,4,5]
squarednumbers=list(map(square,numbers))
print(numbers)
print(squarednumbers)