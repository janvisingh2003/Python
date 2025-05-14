# Login Attempt System

# Predefined credentials
correct_username = "admin"
correct_password = "secure123"

# Get user input
username = input("Enter username: ").strip()
password = input("Enter password: ").strip()

# Check credentials
if username == correct_username and password == correct_password:
    print("Login successful. Welcome!")
else:
    print("Login failed. Incorrect username or password.")
