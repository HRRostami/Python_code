my_name = "Hossein"
password = "W@12"
user_name = input("Please enter your first name: ").capitalize()
if user_name == my_name:
    print(f"Hello, {user_name}! The password is: {password}")
else:
    print(f"Hello, {user_name}! See you later.")