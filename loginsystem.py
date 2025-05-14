# Login System using Membership Operator

# List of allowed usernames
allowed_users = ['john', 'amy', 'sita']

# Get the username from the user
username = input("Enter your username: ").strip().lower()

# Check if the username is allowed
if username in allowed_users:
    print(f"Welcome, {username}!")
else:
    print("Access denied. Username not recognized.")
