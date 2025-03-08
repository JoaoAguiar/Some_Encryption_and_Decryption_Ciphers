import string

# Define the Western alphabet and a dictionary for handling accented characters
WEST_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Base class for cryptographic algorithms
class CryptAlgorithm:
    def __init__(self, alphabet=WEST_ALPHABET):
        self.alphabet = alphabet

    def invert_monoalphabetic(self, key):
        """
        Inverts the monoalphabetic substitution table.

        Args:
            key (str): The key used for substitution.

        Returns:
            str: The inverted substitution alphabet.
        """
        ascii_code = ord('a')
        key_list = list(self.alphabet)

        for i, char in enumerate(key):
            key_list[ord(char) - ascii_code] = chr(ascii_code + i)

        # Combine the list back into a string
        return ''.join(key_list)


# MonoAlphabetic cipher implementation
class MonoAlphabetic(CryptAlgorithm):
    def __init__(self, key, alphabet=WEST_ALPHABET):
        super().__init__(alphabet)
        self.key = complete_key(key, alphabet)

    def encrypt(self, text):
        """
        Encrypts the given text using a monoalphabetic substitution cipher.

        Args:
            text (str): The plaintext to be encrypted.

        Returns:
            str: The encrypted text.
        """
        translation_table = text.maketrans(self.alphabet, self.key)
        return text.translate(translation_table)

    def decrypt(self, text):
        """
        Decrypts the given text using a monoalphabetic substitution cipher.

        Args:
            text (str): The ciphertext to be decrypted.

        Returns:
            str: The decrypted text.
        """
        inverted_key = self.invert_monoalphabetic(self.key)
        translation_table = text.maketrans(self.alphabet, inverted_key)
        return text.translate(translation_table)


def complete_key(key, alphabet):
    """
    Completes a key by appending the remaining characters of the alphabet.

    Args:
        key (str): The initial key.
        alphabet (str): The alphabet to use.

    Returns:
        str: The completed key.
    """
    key = remove_repeats(key.lower())
    return key + ''.join(char for char in alphabet if char not in key)


def remove_repeats(key):
    """
    Removes repeated characters from a string.

    Args:
        key (str): The string to process.

    Returns:
        str: The string with duplicates removed.
    """
    seen = set()
    return ''.join(seen.add(char) or char for char in key if char not in seen)


def count_characters(text):
    """
    Counts and prints the frequency of each character in the text.

    Args:
        text (str): The input text.
    """
    text_length = len(text)
    frequencies = {char: text.count(char) for char in WEST_ALPHABET}

    print("-- Percentage of Characters --")
    for char, count in frequencies.items():
        percentage = (count / text_length) * 100
        print(f"{char} = {percentage:.2f}%")


def count_digraphs(text):
    """
    Counts and prints the frequency of each digraph (two-letter combination) in the text.

    Args:
        text (str): The input text.
    """
    digraphs = {}
    total_digraphs = len(text) - 1

    for i in range(total_digraphs):
        digraph = text[i:i+2]
        digraphs[digraph] = digraphs.get(digraph, 0) + 1

    print("-- Percentage of Digraphs --")
    for digraph, count in sorted(digraphs.items()):
        percentage = (count / total_digraphs) * 100
        print(f"{digraph} = {percentage:.2f}%")