# Cryptography Script Runner

A command-line tool implementing classical cryptographic algorithms for educational purposes and text encryption/decryption.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
- [Supported Algorithms](#supported-algorithms)
  - [Caesar Cipher](#caesar-cipher)
  - [MonoAlphabetic Cipher](#monoalphabetic-cipher)
  - [Vigenère Cipher](#vigenère-cipher)
- [Installation](#installation)
- [Usage](#usage)
  - [Command Syntax](#command-syntax)
  - [Examples](#examples)
- [Advanced Features](#advanced-features)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a unified interface to several classical cryptographic algorithms. Designed for educational purposes, it demonstrates fundamental encryption principles through a clean, modular implementation. Each cipher is implemented as a separate module with consistent interfaces for encryption and decryption operations.

## Features

- **Command-line Interface**: Simple syntax for quick encryption/decryption operations
- **Multiple Cipher Support**: Implementation of three classic cryptographic algorithms
- **Modular Design**: Clean separation between cipher implementations
- **Text Analysis Tools**: Character frequency analysis and cipher detection
- **Visualization**: Graphical analysis of encrypted text patterns (with Vigenère)

## Project Structure

```
.
├── ciphers.py              # Main CLI interface
├── caesar_cipher.py        # Implementation of Caesar cipher
├── monoalphabetic_cipher.py # Implementation of MonoAlphabetic cipher
└── vigenere_cipher.py      # Implementation of Vigenère cipher with analysis tools
```

## Supported Algorithms

### Caesar Cipher

The **Caesar Cipher** is a substitution cipher where each letter is shifted a fixed number of positions down the alphabet.

**Implementation Details:**
- Simple character rotation with modular arithmetic
- Preserves letter case (uppercase/lowercase)
- Maintains non-alphabetic characters unchanged

**Example:**
```
Plaintext:  "joao"
Rotation:   8
Ciphertext: "wvhf"
```

### MonoAlphabetic Cipher

The **MonoAlphabetic Cipher** substitutes each letter according to a key-based mapping, providing more security than Caesar cipher.

**Implementation Details:**
- Key-based character substitution
- Automatic key completion and duplicate character handling
- Statistical analysis tools for character frequency

**Example:**
```
Plaintext:  "joao"
Key:        "ana"
Ciphertext: "rprp"
```

### Vigenère Cipher

The **Vigenère Cipher** is a polyalphabetic substitution method using a repeating key for variable character shifts.

**Implementation Details:**
- Key-based variable shift values
- Preservation of non-alphabetic characters
- Advanced cryptanalysis tools including:
  - Coincidence index calculation
  - Periodicity analysis with graphical output

**Example:**
```
Plaintext:  "joao"
Key:        "ana"
Ciphertext: "xqpy"
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/cryptography-script-runner.git
   cd cryptography-script-runner
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Verify installation by running a test command:
   ```bash
   python ciphers.py ceaser hello 3
   ```

## Usage

### Command Syntax

The general command format follows this pattern:

```bash
python ciphers.py <cipher_name> <text> <key_or_rotation>
```

Where:
- `<cipher_name>`: Algorithm to use (`ceaser`, `mono`, or `vigenere`)
- `<text>`: Text to encrypt/decrypt
- `<key_or_rotation>`: Numeric rotation for Caesar, or string key for others

### Examples

#### 1. Caesar Cipher

```bash
python ciphers.py ceaser joao 8
```

Output:
```
***** CAESAR CIPHER *****
Encrypted Text: wvhf
Decrypted Text: joao
```

#### 2. MonoAlphabetic Cipher

```bash
python ciphers.py mono joao ana
```

Output:
```
***** MONOALPHABETIC CIPHER *****
Encrypted Text: rprp
Decrypted Text: joao
```

#### 3. Vigenère Cipher

```bash
python ciphers.py vigenere joao ana
```

Output:
```
***** VIGENERE CIPHER *****
Encrypted Text: xqpy
Decrypted Text: joao
```