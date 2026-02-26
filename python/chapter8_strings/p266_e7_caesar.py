# Write a program to encode and decode a message based on a Ceasar cipher.
# The input should be plaintext and the value of the key.
# The output should be an encoded message where each character in the original message is replaced by shifting it key characters in the Unicode character set.
# The map should wrap such as z + 1 = a
# Hint: Create one big string

def main():
    print("This program will encode / decode a message based upon a Caesar cipher of some key.\n")

    message = input("Enter the message: ")
    key = int(input("Enter the key: "))
    print()

    all_characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ `1234567890-=~!@#$%^&*()_+[]\\{}|;':\",./<>?"

    encoded = ""
    for character in message:
        idx = all_characters.find(character)
        idx = (idx + key) % len(all_characters)
        encoded += all_characters[idx]
    
    print("Result:", encoded)
    print()
    print("Key to reverse the process will be:", -key)

if __name__ == "__main__":
    main()