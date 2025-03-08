import matplotlib.pyplot as plt

# Default alphabet
WEST_ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Base class for cryptographic algorithms
class CryptAlgorithm:
    def __init__(self, alphabet=WEST_ALPHABET):
        self.alphabet = alphabet

    # Inverts a monoalphabetic substitution cipher key
    def invert_monoalphabetic(self, key):
        inverted_key = [''] * len(self.alphabet)
        for i, char in enumerate(key):
            inverted_key[ord(char) - ord('a')] = self.alphabet[i]
        return ''.join(inverted_key)


# Vigenere cipher class for encryption and decryption
class Vigenere(CryptAlgorithm):
    def __init__(self, key, alphabet=WEST_ALPHABET):
        super().__init__(alphabet)
        self.key = key.lower()
        self.key_length = len(key)
        self.alphabet_length = len(alphabet)

    # Encrypts the text using the Vigenere cipher
    def encrypt(self, text):
        encrypted_message = []
        key_index = 0

        for char in text:
            if char in self.alphabet:
                shift = ord(self.key[key_index % self.key_length]) - ord('a')
                new_char = self.alphabet[(ord(char) - ord('a') + shift) % self.alphabet_length]
                encrypted_message.append(new_char)
                key_index += 1
            else:
                # Preserve non-alphabetic characters
                encrypted_message.append(char)

        return ''.join(encrypted_message)

    # Decrypts the text using the Vigenere cipher
    def decrypt(self, text):
        decrypted_message = []
        key_index = 0

        for char in text:
            if char in self.alphabet:
                shift = ord(self.key[key_index % self.key_length]) - ord('a')
                new_char = self.alphabet[(ord(char) - ord('a') - shift) % self.alphabet_length]
                decrypted_message.append(new_char)
                key_index += 1
            else:
                # Preserve non-alphabetic characters
                decrypted_message.append(char)

        return ''.join(decrypted_message)


# Counts and prints character frequency as percentages
def count_characters(text, alphabet=WEST_ALPHABET):
    char_count = {char: 0 for char in alphabet}
    total_chars = 0

    for char in text:
        if char in char_count:
            char_count[char] += 1
            total_chars += 1

    print("-- Character Frequency --")
    for char, count in char_count.items():
        if total_chars > 0:
            percentage = (count / total_chars) * 100
            print(f"{char}: {percentage:.2f}%")
        else:
            print(f"{char}: 0.00%")


# Divides text into periodic chunks
def divide_text(text, period):
    chunks = ['' for _ in range(period)]
    for i, char in enumerate(text):
        chunks[i % period] += char
    return chunks


# Calculates the index of coincidence for a given text
def coincidence_index(text):
    char_count = {char: 0 for char in WEST_ALPHABET}
    for char in text:
        if char in char_count:
            char_count[char] += 1

    total_chars = sum(char_count.values())
    if total_chars < 2:
        return 0

    index = sum(count * (count - 1) for count in char_count.values())
    denominator = total_chars * (total_chars - 1)
    return index / denominator


# Analyzes periodicity in the text
def analyze_periodicity(text, max_period=50):
    periodicity = []

    for period in range(2, max_period):
        chunks = divide_text(text, period)
        average_index = sum(coincidence_index(chunk) for chunk in chunks) / period
        periodicity.append(average_index)

    # Plot the periodicity results
    plt.scatter(range(2, max_period), periodicity, color="green", marker="*", s=50)
    plt.xlabel("Period")
    plt.ylabel("Index of Coincidence")
    plt.title("Periodicity Analysis")
    plt.show()
