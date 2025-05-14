# Password Strength Checker

# Get the password input from the user
password = input("Enter your password: ")

# Check the strength of the password
if len(password) >= 8 and '@' in password:
    print("Password is strong.")
else:
    print("Password is weak. It must be at least 8 characters long and contain '@'.")
