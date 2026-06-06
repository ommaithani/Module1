# Practical Example 8: Write a Python program to check if a person is eligible to donate blood 
# using a nested if.

while True:
    age=int(input("Enter Your age : "))
    if age>=18:
        weight=int(input("Enter Your weight : "))
        if weight>=50:
            print("You can Donate Blood")
        else:
            print("Your weight is below 50kg, you cannot donate blood")
    else:
        print("Your age is below 18, you cannot donate blood")