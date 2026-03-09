# Each letter gets shifted a fixed number of positions
# Non-letter characters stay unchanged.
# Wrap around so that Z shifts back to A

def encrypt_caesar(text, shift):
    result = ""
    for char in text:
        if not char.isalpha():
            result += char
            continue
        base = ord("A") if char.isupper() else ord("a")
        result += chr((ord(char) - base + shift) % 26 + base)
    return result

def main():
    print("Caesar Cipher")
    text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the key (1-25): "))
    encrypted = encrypt_caesar(text, shift)
    print("Encrypted:", encrypted)

if __name__ == "__main__":
    main()