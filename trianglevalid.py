# Triangle Validity Checker

# Get the lengths of the three sides from the user
a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))
c = float(input("Enter length of side C: "))

# Check triangle validity using the triangle inequality theorem
if a + b > c and a + c > b and b + c > a:
    print("The sides can form a valid triangle.")
else:
    print("The sides cannot form a valid triangle.")
