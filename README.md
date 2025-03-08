# Cryptography Script Runner

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Version](https://img.shields.io/badge/version-1.0.0-green.svg)

A command-line tool implementing classic cryptography algorithms for educational purposes.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Supported Algorithms](#supported-algorithms)
  - [Caesar Cipher](#caesar-cipher)
  - [MonoAlphabetic Cipher](#monoalphabetic-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
- [Installation](#installation)
- [Usage](#usage)
  - [Syntax](#syntax)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Overview

This tool provides a simple interface to encrypt and decrypt text using three classic cryptographic algorithms. It's designed for educational purposes to demonstrate the principles of basic encryption techniques.

## Features

- Easy-to-use command-line interface
- Support for multiple classic ciphers
- Both encryption and decryption functionality
- Minimal dependencies

## Supported Algorithms

### Caesar Cipher

The **Caesar Cipher** is a simple substitution algorithm where each letter in the text is shifted by a fixed number of positions in the alphabet. The rotation is the number that defines the shift. For example, if the rotation is 3, the letter "a" will be replaced by "d", "b" by "e", and so on.

**Example**:
- Original text: "joao"
- Rotation: 8
- Encrypted text: "wvhf"

### MonoAlphabetic Cipher

The **MonoAlphabetic Cipher** is a type of substitution cipher where each letter of the alphabet is mapped to another letter of the alphabet according to a provided key. The key is a string that replaces the letters of the original alphabet.

**Example**:
- Original text: "joao"
- Key: "ana"
- Encrypted text: "rprp"

In this case, the letter "j" is replaced by the corresponding letter in the key "ana", and so on.

### Vigenère Cipher

The **Vigenère Cipher** is a polyalphabetic encryption algorithm that uses a key composed of multiple letters. Unlike the Caesar Cipher, which applies the same shift to all letters, the Vigenère Cipher applies a different shift for each letter, depending on the position of the letter in the key. The key is repeated throughout the text, and each letter of the text is shifted based on the value of the corresponding letter in the key.

**Example**:
- Original text: "joao"
- Key: "ana"
- Encrypted text: "xqpy"

The key "ana" is repeated to match the length of the text, and each letter of the text is shifted according to the position of the corresponding letter in the key.

## Installation

1. Clone the repository to your computer.
2. Make sure the cryptography scripts are in the same directory as the main script (`ciphers.py`).
3. If you don't have the necessary libraries installed yet, install them:

   ```bash
   pip install matplotlib
   ```

## Usage

The script allows you to run any of the three encryption algorithms directly from the command line. Simply pass the name of the desired algorithm, the text to be encrypted/decrypted, and a key or rotation.

### Syntax

```bash
python ciphers.py <cipher_name> <text> <key or rotation>
```

Where:
- `<cipher_name>`: the name of the cipher to run: `ceaser`, `mono`, or `vigenere`.
- `<text>`: the text you want to encrypt or decrypt.
- `<key or rotation>`: for the **Caesar Cipher** it is the numerical rotation (an integer). For **MonoAlphabetic** and **Vigenère**, you need to provide an encryption key (a string).

### Examples

#### 1. **Caesar Cipher**

```bash
python cipher.py ceaser joao 8
```
```
***** CAESAR CIPHER *****
Encrypted Text: wvhf
Decrypted Text: joao
```

#### 2. **MonoAlphabetic Cipher**

```bash
python cipher.py mono joao ana
```
```
***** MONOALPHABETIC CIPHER *****
Encrypted Text: rprp
Decrypted Text: joao
```

#### 3. **Vigenère Cipher**

```bash
python cipher.py vigenere joao ana
```
```
***** VIGENERE CIPHER *****
Encrypted Text: xqpy
Decrypted Text: joao
```

## Contributing

Contributions are welcome! Please read the [contributing guidelines](CONTRIBUTING.md) first.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

