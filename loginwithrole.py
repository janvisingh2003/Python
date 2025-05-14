# Login with Role

# List of allowed usernames
allowed_users = ['john', 'amy', 'sita']

# Allowed roles
allowed_roles = ['admin', 'manager']

# Get user input
username = input("Enter your username: ").strip().lower()
role = input("Enter your role (admin/manager): ").strip().lower()

# Check conditions
if username in allowed_users and role in allowed_roles:
    print(f"Login successful. Welcome, {username} ({role}).")
else:
    print("Login failed. Invalid username or role.")
