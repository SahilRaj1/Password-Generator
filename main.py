import string
import random

if __name__ == "__main__":
    
    # Create a list to store all the possible characters
    plist = []

    # Add the lists of the set of characters to plist
    plist.extend(list(string.ascii_lowercase))
    plist.extend(list(string.ascii_uppercase))
    plist.extend(list(string.digits))
    plist.extend(list("!@#$%^&*()/\><_-"))  # could've used 'string.punctuation' function

    # Shuffling the items in the list plist
    random.shuffle(plist)

    # Finally asking the user for the length of the password and displaying the genrated password
    print()
    n = int(input("Enter the length of password you require: "))
    print("Your generated password is", "\033[1m" + "".join(plist[:n]) + "\033[0m" + "\n")
