def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.
    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    ciphertext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in plaintext:
        if letter.lower() not in alphabet:
            ciphertext += letter
            continue
        if letter == letter.lower():
            ciphertext += alphabet[(alphabet.index(letter) + shift) % 26] 
        else:
            ciphertext += alphabet[(alphabet.index(letter.lower()) + shift) % 26].upper()
    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.
    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in ciphertext:
        if letter.lower() not in alphabet:
            plaintext += letter
            continue
        if letter == letter.lower():
            plaintext += alphabet[(alphabet.index(letter) - shift) % 26] 
        else:
            plaintext += alphabet[(alphabet.index(letter.lower()) - shift) % 26].upper()
    return plaintext