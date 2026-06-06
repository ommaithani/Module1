# Write a Python program that manipulates and prints strings using various string methods.

text='   Learning Python   '
print(f"'{text}'")

# Stripping
cleantext=text.strip()
print(f"Removed spaces using strip():'{cleantext}'")

# Changing 
print(f"Lowercase using lower():'{cleantext.lower()}")
print(f"Uppercase using upper():'{cleantext.upper()}")
print(f"Title case using title():'{cleantext.title()}")

# Replacing 
replacetext=cleantext.replace("Python","Python with django")
print(f"Replace using replace():'{replacetext}")

# Splitting
splittext=cleantext.split()
print(f"Split using split():'{splittext}")

# Finding position
position=cleantext.find("Python")
print(f"Finding using find():'{position}")
