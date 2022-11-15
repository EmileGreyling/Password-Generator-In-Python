import string
from random import choice

# Ask the user for the length of the password
password_length = int(input("Password Length (8 is recommended): "))

# Ask the user for the number of password to be generated
password_count = int(input("How many passwords do you want? "))

# Store all the characters for a password in variables

# Letters
letters = string.ascii_letters

# Numbers 
numbers = string.digits

# Special Characters like !@#$
special_chars = string.punctuation

# Store all characters into one variable
all_chars = letters + numbers + special_chars

"""Generate Password"""

print()

for password in range(password_count):
    password = ""
    while len(password) != password_length:
        password_char = choice(all_chars)
        password += password_char  
    
    # Print out new password
    print(f"Password Suggestion: {password}")
