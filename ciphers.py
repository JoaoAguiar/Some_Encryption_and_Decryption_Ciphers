import sys
import caesar_cipher
import monoalphabetic_cipher
import vigenere_cipher

def main():
    if len(sys.argv) < 2:
        print("Usage: python new_script.py <script_name> <text> [key/rotation]")
        sys.exit(1)

    # Extract command-line arguments
    script_name = sys.argv[1].lower()  # Script to run: 'ceaser', 'mono', or 'vigenere'
    text = sys.argv[2]                # The text to be processed
    additional_arg = sys.argv[3] if len(sys.argv) > 3 else None  # Key or rotation value

    if script_name == "ceaser":
        print("***** CAESAR CIPHER *****")

        if additional_arg is None or not additional_arg.isdigit():
            print("For Caesar cipher, provide a numeric rotation as the third argument.")
            sys.exit(1)
        
        rotation = int(additional_arg)

        print("Encrypted Text:", caesar_cipher.encrypt(text, rotation))
        print("Decrypted Text:", caesar_cipher.decrypt(caesar_cipher.encrypt(text, rotation), rotation))

    elif script_name == "mono":
        print("***** MONOALPHABETIC CIPHER *****")

        if additional_arg is None:
            print("For MonoAlphabetic cipher, provide a key as the third argument.")
            sys.exit(1)

        key = additional_arg
        cipher = monoalphabetic_cipher.MonoAlphabetic(key)

        print("Encrypted Text:", cipher.encrypt(text))
        print("Decrypted Text:", cipher.decrypt(cipher.encrypt(text)))

    elif script_name == "vigenere":
        print('***** VIGENERE CIPHER *****')

        if additional_arg is None:
            print("For Vigenere cipher, provide a key as the third argument.")
            sys.exit(1)
        
        key = additional_arg
        cipher = vigenere_cipher.Vigenere(key)
        
        print("Encrypted Text:", cipher.encrypt(text))
        print("Decrypted Text:", cipher.decrypt(cipher.encrypt(text)))

    else:
        print(f"Unknown script name '{script_name}'. Use 'ceaser', 'mono', or 'vigenere'.")
        sys.exit(1)

if __name__ == "__main__":
    main()