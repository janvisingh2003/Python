# Eligibility for Voting and Driving

# Get age from the user
age = int(input("Enter your age: "))

# Determine eligibility
if age >= 21:
    print("You are eligible for both voting and driving.")
elif age >= 18:
    print("You are eligible for voting but not for driving.")
elif age >= 0:
    print("You are not eligible for voting or driving.")
else:
    print("Invalid age entered.")
