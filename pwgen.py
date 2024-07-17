import random
import string
import logging

# Set logging level to WARNING to suppress debug messages
logging.basicConfig(level=logging.WARNING)

def generate_password(length=12):
    """Generate a random password containing letters, digits, and punctuation."""
    if length < 4:
        raise ValueError("Password length should be at least 4")

    logging.debug("Generating a password of length %d", length)

    # Create a pool of characters
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password has at least one character from each category
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the list to ensure randomness
    random.shuffle(password)

    # Convert list to string
    logging.debug("Generated password: %s", ''.join(password))
    return ''.join(password)

def main():
    while True:
        try:
            length = int(input("Enter the desired password length (at least 4): "))
            if length < 4:
                raise ValueError("Password length should be at least 4")
            password = generate_password(length)
            print("Generated password:", password)
            break
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

if __name__ == "__main__":
    main()
