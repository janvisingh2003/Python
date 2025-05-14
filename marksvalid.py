# Marks Validity Check

# Get the mark from the user
mark = float(input("Enter the mark: "))

# Check if the mark is valid
if 0 <= mark <= 100:
    print("The mark is valid.")
else:
    print("Invalid mark. It must be between 0 and 100.")
