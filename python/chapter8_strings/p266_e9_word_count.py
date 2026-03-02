# Write a program that counts the number of words in a sentence entered by the user

def main():
    print("This program will count the number of words in a sentence.")
    print()

    sentence = input("Enter the sentence(s): ")
    print()

    count = len(sentence.split())
    print("Number of words:", count)

if __name__ == "__main__":
    main()