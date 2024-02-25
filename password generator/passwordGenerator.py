import random
import string

def generate_password(length=12, include_uppercase=True, include_digits=True, include_special_chars=True):
    # Define character sets
    uppercase_letters = string.ascii_uppercase if include_uppercase else ''
    lowercase_letters = string.ascii_lowercase
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special_chars else ''

    # Combine character sets
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars

    # Check if the length is valid
    if length < 8:
        print("Password length should be at least 8.")
        return None

    # Ensure at least one character from each set is included
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_chars)

    # Fill the remaining length with random characters
    remaining_length = length - 4
    password += ''.join(random.choice(all_chars) for _ in range(remaining_length))

    # Shuffle the password to randomize the order
    password_list = list(password)
    random.shuffle(password_list)
    shuffled_password = ''.join(password_list)

    return shuffled_password

# Example usage
length = int(input("Enter the desired password length: "))
include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
include_digits = input("Include digits? (yes/no): ").lower() == 'yes'
include_special_chars = input("Include special characters? (yes/no): ").lower() == 'yes'

password = generate_password(length, include_uppercase, include_digits, include_special_chars)
print("Generated Password:", password)
