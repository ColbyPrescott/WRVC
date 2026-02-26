# Write a program that allows the user to type in a phrase and then outputs the acronym for that phrase.
# Note: The acronym should be all uppercase, even if the words in the phrase are not capitalized

def main():
    print("This program will take a phrase and turn it into an acronym.\n")

    phrase = input("Enter the phrase to acronymify: ")

    print("\nAcronym: ", end="")
    words = phrase.split()
    for word in words:
        print(word[0].upper(), end="")
    
if __name__ == "__main__":
    main()