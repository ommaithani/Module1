# Practical Example 3: Write a Python program to find a specific string in the list using a simple 
# for loop and if condition. 

list=[10,20,30]
item=10
for i in list:
    if i==item:
        print("item found")
        break

# or

# while True:
#     list=[1,2,3]
#     guess=int(input("Enter a number: "))
#     for i in list:
#         if i==guess:
#             print("item found")
#             break
#     # else:
#     #     print("item not found")