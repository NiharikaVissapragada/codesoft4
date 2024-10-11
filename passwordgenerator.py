import random
import string

def generate_password(length):
    # Define the character sets to use
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Combine all character sets
    all_characters = lower + upper + digits + symbols
    
    # Generate a random password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    while True:
        try:
            # Prompt user for password length
            length = int(input("Enter desired password length (minimum 4): "))
            if length < 4:
                print("Password length should be at least 4 characters. Please try again.")
                continue

            # Generate and display the password
            password = generate_password(length)
            print(f"Generated Password: {password}")
            break  # Exit the loop after successful generation

        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
