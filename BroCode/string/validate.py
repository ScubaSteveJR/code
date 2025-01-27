# Validate user input
# username is no more than 12 chars
# username must not contain spaces
# username must not contain digits

username = input("Enter a username: ")
username.find(" ")

if len(username) > 12:
    print("Your username can't be more than 12 chars.")
elif not username.find(" ") == -1:
    print("Your username can not contain spaces.")
elif not username.isalpha():
    print("Your username can not contain digits.")
else:
    print(f"Welcome {username}")
