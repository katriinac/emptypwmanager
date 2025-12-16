import json
import re
import random
import string

# Caesar cipher encryption and decryption functions (pre-implemented)
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_decrypt(text, shift):
    return caesar_encrypt(text, -shift)

# Password strength checker function (optional)
def is_strong_password(password):
    # ...

# Password generator function (optional)
def generate_password(length):
# Generate a random strong password of the specified length.
# Args: length (int): The desired length of the password.
# Returns: str: A random strong password.
  if length < 8: 
        length = 8 # antaa 8 merkkiä vaikka valittaisiin alle 8
    characters = string.ascii_letters + string.digits + string.punctuation # kaikki aakkoset, numerot ja erikoismerkit
    return ''.join(random.choice(characters) for _ in range(length)) # arvotaan satunnaiset merkit, .join yhdistää ne merkkijonoksi

# Initialize empty lists to store encrypted passwords, websites, and usernames
encrypted_passwords = []
websites = []
usernames = []

# Function to add a new password 
def add_password():
    """
    Add a new password to the password manager.

    This function should prompt the user for the website, username,  and password and store them to lits with same index. Optionally, it should check password strengh with the function is_strong_password. It may also include an option for the user to
    generate a random strong password by calling the generate_password function.

    Returns:
        None
    """

# Function to retrieve a password 
def get_password():
    """
    Retrieve a password for a given website.

    This function should prompt the user for the website name and
    then display the username and decrypted password for that website.

    Returns:
        None
    """

# Function to save passwords to a JSON file 
def save_passwords():
    """
    Save the password vault to a file.

    This function saves passwords, websites, and usernames to a file
    named "vault.txt" in a structured JSON format.
    """
    # Combine the parallel lists into a list of dictionaries for a structured format
    vault_data = []
    for i in range(len(websites)):
        entry = {
            "website": websites[i],
            "username": usernames[i],
            "password": passwords[i]
        }
        vault_data.append(entry)

    try:
        # Open the file in write mode ('w')
        with open("vault.txt", "w") as f:
            # Use json.dump to write the list of dictionaries to the file
            # indent=4 makes the file human-readable
            json.dump(vault_data, f, indent=4)
        print("Passwords saved successfully to vault.txt")
    except IOError as e:
        # Handle potential file writing errors
        print(f"Error: Could not save passwords to file. {e}")


# Function to load passwords from a JSON file 
def load_passwords():
    """
    Load passwords from a file into the password vault.

    This function loads passwords, websites, and usernames from a
    file named "vault.txt" and populates the respective lists.
    """
    try:
        # Open the file in read mode ('r')
        with open("vault.txt", "r") as f:
            # Load the data from the file
            vault_data = json.load(f)
            
            # Clear current lists to prevent duplication on reload
            websites.clear()
            usernames.clear()
            passwords.clear()

            # Populate the lists from the loaded data
            for entry in vault_data:
                websites.append(entry["website"])
                usernames.append(entry["username"])
                passwords.append(entry["password"])
        
        print("Passwords loaded successfully from vault.txt")

    except FileNotFoundError:
        # This is expected on the first run, so we just print a message
        print("No existing vault file found. A new one will be created when you save.")
    except (json.JSONDecodeError, KeyError) as e:
        # Handle cases where the file is corrupted or has an unexpected format
        print(f"Error: Could not read or parse vault.txt. The file might be corrupted. {e}")


  # Main
def main():
# implement user interface 

  while True:
    print("\nPassword Manager Menu:")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Save Passwords")
    print("4. Load Passwords")
    print("5. Quit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_password()
    elif choice == "2":
        get_password()
    elif choice == "3":
        save_passwords()
    elif choice == "4":
        passwords = load_passwords()
        print("Passwords loaded successfully!")
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")

# Execute the main function when the program is run
if __name__ == "__main__":
    main()
