# Write a Python program to demonstrate string slicing.

text='PROGRAMMING'
print(f"Original string: '{text}'")
slice1=text[0:7]
print(slice1)

slice2=text[:5]
print(slice2)

slice3=text[7:]
print(slice3)

slice4=text[-5:]
print(slice4)

slice5=text[:-4]
print(slice5)

slice6=text[::2]
print(slice6)

slice7=text[::-1]
print(slice7)