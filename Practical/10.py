# Practical Example 7: Write a Python program to calculate grades based on percentage using 
# if-else ladder. 

while True:
    a=int(input("Enter your Marks : "))
    if a>=80 and a<=100:
        print("A Grade")
    elif a>=70 and a<80:
        print("B Grade")
    elif a>=50 and a<70:
        print("C Grade")
    elif a>=35 and a<50:
        print("D Grade")
    else:
        print("Fail")