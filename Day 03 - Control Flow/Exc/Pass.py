from getpass import getpass

password = getpass("Enter password: ")
print("Password received")

username = input("Enter username: ")

correct_username = "admin"
correct_password = "1234"

if username == correct_username and password == correct_password:
    print("Login successful!")
else:
    print("Invalid username or password")