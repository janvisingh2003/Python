# Age Group Classifier

age = int(input("Enter the person's age: "))

if age < 0:
    category = "Invalid age entered"
elif age < 13:
    category = "Child"
elif age <= 19:
    category = "Teen"
elif age <= 59:
    category = "Adult"
else:
    category = "Senior"

# Display the result
print(f"Age: {age}")
print(f"Category: {category}")
