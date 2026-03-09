# The XOR operation is the foundation of mdoern stream ciphers
# XOR-ing the same key twice returns the origina, so encryption and decryption are identical operations
# XOR every character's ASCII value with a single key byte (0-255)

def xor_cipher(text, key):
    result = ""
    for char in text:
        result += chr(ord(char) ^ key)
    return result

def main():
    print("XOR Cipher")
    text = input("Enter the message to encrypt / decrypt: ")
    key = int(input("Enter the key (0-255): "))
    print("Result:", xor_cipher(text, key))

if __name__ == "__main__":
    main()