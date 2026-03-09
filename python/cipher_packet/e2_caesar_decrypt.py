# Each letter gets shifted a fixed number of positions
# Non-letter characters stay unchanged.
# Wrap around so that Z shifts back to A

from e1_caesar_cipher import encrypt_caesar

def decrypt_caesar(text, shift):
    return encrypt_caesar(text, -shift)

def main():
    print("Caesar Cipher")
    text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the key (1-25): "))
    decrypted = decrypt_caesar(text, shift)
    print("Decrypted:", decrypted)

if __name__ == "__main__":
    main()