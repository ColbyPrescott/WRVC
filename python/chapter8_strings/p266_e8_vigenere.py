# Write a program to encode and decode a message based on a Vigenère cipher
# The input should be plaintext and the passphrase.
# The output should be an encoded message where each character is shifted X times
# where X is the numeric value of the letter in the passphrase that corresponds with that character in the original message
# Ex: Encoding "Feed me" with the passphrase "cat" will shift "F" by 2 (c), "e" by 0 (a), "e" by 20, "d" by 2 (c), etc.

def main():
    print("This program will encode / decode a message based upon a Vigenère cipher of some passphrase.\n")

    message = input("Enter the message: ")
    passphrase = input("Enter the passphrase: ")

    decoding = None
    while decoding != "E" and decoding != "D":
        decoding = input("Encode or decode (E/D)? ").upper()[0]
    decoding = decoding == "D"

    print()

    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ `1234567890-=~!@#$%^&*()_+[]\\{}|;':\",./<>?"

    encoded = ""
    for i in range(len(message)):
        char = message[i]
        char_idx = all_characters.find(char)

        key = passphrase[i % len(passphrase)]
        key_idx = all_characters.find(key)
        if decoding:
            key_idx *= -1

        new_idx = (char_idx + key_idx) % len(all_characters)
        encoded += all_characters[new_idx]
    
    print("Result:", encoded)

if __name__ == "__main__":
    main()