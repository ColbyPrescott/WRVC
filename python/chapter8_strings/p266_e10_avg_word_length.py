# Write a program that calcualtes the average number of characters in each word of a sentence

def main():
    print("This program will calculate the average number of characters in each word of a sentence or more.")
    print()

    sentence = input("Enter the sentence(s): ")
    print()

    words = sentence.split()
    sum = 0
    for word in words:
        sum += len(word)
    avg = sum / len(words)

    print("Average word length:", avg)

if __name__ == "__main__":
    main()