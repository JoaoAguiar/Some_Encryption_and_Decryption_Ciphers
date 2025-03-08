# Caesar Cipher Implementation
# This script encrypts or decrypts text using a Caesar cipher with a given rotation value.

def encrypt(text, rotation):
    """
    Encrypts the given text using a Caesar cipher with the specified rotation.
    
    Formula for encryption:
    encrypt(letter, n) = (letter + n) mod 26
    
    Args:
        text (str): The plaintext to be encrypted.
        rotation (int): The number of positions to rotate each character.

    Returns:
        str: The encrypted text.
    """
    encrypted_message = ""

    for character in text:
        if character.isupper():  # Handle uppercase letters
            # 'A' has an ASCII value of 65
            encrypted_message += chr(((ord(character) - 65 + rotation) % 26) + 65)
        elif character.islower():  # Handle lowercase letters
            # 'a' has an ASCII value of 97
            encrypted_message += chr(((ord(character) - 97 + rotation) % 26) + 97)
        else:
            # Non-alphabetic characters are added unchanged
            encrypted_message += character

    return encrypted_message


def decrypt(text, rotation):
    """
    Decrypts the given text using a Caesar cipher with the specified rotation.
    
    Formula for decryption:
    decrypt(letter, n) = (letter - n) mod 26
    
    Args:
        text (str): The ciphertext to be decrypted.
        rotation (int): The number of positions to rotate each character back.

    Returns:
        str: The decrypted text.
    """
    decrypted_message = ""

    for character in text:
        if character.isupper():  # Handle uppercase letters
            decrypted_message += chr(((ord(character) - 65 - rotation) % 26) + 65)
        elif character.islower():  # Handle lowercase letters
            decrypted_message += chr(((ord(character) - 97 - rotation) % 26) + 97)
        else:
            # Non-alphabetic characters are added unchanged
            decrypted_message += character

    return decrypted_message
