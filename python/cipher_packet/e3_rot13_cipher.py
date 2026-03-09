# The ROT13 is a special version of the Caesar cipher that will shift by 13, exactly half the alphabet

from e1_caesar_cipher import encrypt_caesar

def rot13(text):
    return encrypt_caesar(text, 13)

def main():
    print("ROT13 Cipher")
    text = input("Enter the text to encrypt: ")
    encrypted = rot13(text)
    print("Encrypted:", encrypted)

if __name__ == "__main__":
    main()