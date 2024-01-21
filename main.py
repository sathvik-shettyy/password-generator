#basic password generator-sathvik shetty
import random
import string

def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Password Generator!")
    
    # Set default password length to 12 characters
    password_length = 12
    
    try:
        # Get user input for password length
        password_length = int(input("Enter the desired password length (default is 12): "))
    except ValueError:
        print("Invalid input. Using default password length.")

    # Generate and print the password
    password = generate_password(password_length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()