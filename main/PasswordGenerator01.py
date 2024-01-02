import random
import string


# Defining the password generator
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters # alphabets, lower and upper case
    digits = string.digits         # numbers from 0-9
    special = string.punctuation   # different kinds of special characters

    # Because we will always have a password with characters
    characters = letters 

    # In the case of numbers being included but not special characters:
    if numbers:
        characters += digits
    # In the case of special characters being included but not numbers:
    if special_characters:
        characters += special

    # Where we will store the password:
    pwd = ""

    # A variable to check if the password meets the user given criteria:
    meets_criteria = False

    # To help with meeting the criteria further
    # Lets add a variable which checks if the password atleast has one number:
    has_number = False

    # And a variable which checks if the password atleast has one special character:
    has_special = False
    

    # Loop to add random characters (Criteria and length ensurement)
    while not meets_criteria or len(pwd) < min_length:

        # Makes a password with the chosen criteria
        new_char = random.choice(characters)
        pwd += new_char

        # Checking if the password has atleast one digit in it:
        if new_char in digits:
            has_number = True
        # Checking if the password has atleast one special char in it:
        elif new_char in special:
            has_special = True

        # Putting it as true to check if it can turn false because of any criteria not meeting:
        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    # We have finally made the password! 
    return pwd
    

# Making output fancier
min_length = int(input("Enter the minimum length: "))
has_number = input("Do you want to have numbers (y/n)?: ").lower() == "y"
has_special = input("Do you want to have special characters (y/n)?: ").lower() == "y"
pwd = generate_password(min_length, has_number, has_special)
print(f"The generated password is: {pwd}")

# Output would look like (Example): 
# Enter the minimum length: 20
# Do you want to have numbers (y/n)?: y
# Do you want to have special characters (y/n)?: y
# The generated password is: K.a#O+C[+ZaciP(!Bszq0
