import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    password_length = int(input("Enter desired password length: "))

    # Check if the entered password length is less than 8
    if password_length < 8:
        print("Desired password must be at least 8 characters.")
    # Check if the entered password length is greater than 16
    elif password_length > 16:
        print("Password length is capped at 16 characters.")
    else:
        # Generate and display the password if it's between 8 and 16 characters
        generated_password = generate_password(password_length)
        print("Here is your password:", generated_password)
