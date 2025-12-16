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
    website = input("Enter website: ") #kysyy sivua
    username = input("Enter username: ") #kysyy käyttäjätunnusta
    genpass = input("Generate a random password? (yes or no): ").lower() #kysyy luodaanko salasana valmiiksi ja vaihtaa vastaksen pieniin kirjaimiin

    if genpass == "yes": #jos vastasi kyllä
        password = generate_password(12) #luodaan salasana joka on 12 merkkiä pitkä
        print(f"Generated password: {password}") #printataa luotu salasana
    else: #jos vastaus on ei
        password = input("Enter password: ") #syöttää käyttäjä itse salasanan
    encrypted = caesar_encrypt(password, 3) #salataan se jolloin shift on 3

    websites.append(website) #lisätään listaan tiedot
    usernames.append(username) 
    encrypted_passwords.append(encrypted)

    print("Password added successfully")

# Function to retrieve a password 
def get_password():
    if not websites:
        print("No passwords stored yet.") #tarkistetaan onko salasanoja tallenettu
        return
    website = input("Enter website: ") #kysytään käyttäjältä verkkosivun nimi
    if website in websites:            #tarkistetaan löytyykö verkkosivu listalta
        index = websites.index(website) #haetaan sivun indeksi
        encrypted = encrypted_passwords[index] #haetaan salattu salasana ja käyttäjätunnus
        username = usernames[index]
    
        decrypted_password = caesar_decrypt(encrypted, 3) #puretaan salasana Caesar-salauksesta (shift=3)
    
        print("\nPassword found:")
        print(f"Website: {website}")
        print(f"Username: {username}")
        print(f"Password: {decrypted_password}")
    else:
        print("No password found for this website.") #jos verkkosivua ei löydy

# Function to save passwords to a JSON file 
def save_passwords():
 """
    Save the password vault to a file.

    This function should save passwords, websites, and usernames to a text
    file named "vault.txt" in a structured format.

    Returns:
        None
    """

    Returns:
        None
    """

# Function to load passwords from a JSON file 
def load_passwords():
     """
    Load passwords from a file into the password vault.

    This function should load passwords, websites, and usernames from a text
    file named "vault.txt" (or a more generic name) and populate the respective lists.

    Returns:
        None

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
