default_password = "LetMeIn"
password = input("Enter your password: ")
counter = 0

while ((default_password != password) & (counter < 3)):
    print(f"Incorrect password, {3-counter} attempts remaining.")
    password = input("Enter your password: ")
    counter = counter+1

if (default_password == password):
    print("Password correct")
else:
    print("0 attemps remaining.")