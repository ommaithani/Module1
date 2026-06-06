# Practical Example 5: Write a Python program to find greater and less than a number using 
# if_else.

a=10
b=20
if a<b:
    print("B is greater than A")
else:
    print("A is Greater than B")

while True:
    a=int(input("Enter your first number: "))
    b=int(input("Enter your second number: "))
    if a<b:
        print("B is Greater")
    elif a==b:
        print("Both are equal")
    else:
        print("A is Greater")