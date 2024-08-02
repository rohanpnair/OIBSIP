import random
import string

def generaterandompassword(length, use_letters=True, use_numbers=True, use_symbols=True):
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation
    char_pool = ''
    if use_letters:
        char_pool += letters
    if use_numbers:
        char_pool += numbers
    if use_symbols:
        char_pool += symbols

    if not char_pool:
        raise ValueError("At least one character type must be selected.")
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    try:
        length = int(input("Enter the desired password length: "))
        use_letters = input("Include letters? (yes/no): ").strip().lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").strip().lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").strip().lower() == 'yes'
        password = generaterandompassword(length, use_letters, use_numbers, use_symbols)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Invalid input: {e}")

if __name__ == "__main__":
    main()
