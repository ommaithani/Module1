# Write a Python program that uses a custom iterator to iterate over a list of integers.

def myiterator(numbers):
    for num in numbers:
        yield num
mylist=[10,20,30,40,50]
print("iterating over the list:")
for item in myiterator(mylist):
    print(item)

