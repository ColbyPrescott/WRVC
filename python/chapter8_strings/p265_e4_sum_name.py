# Write a program that will take each letter in a name,
# map each letter to a number corresponding with its place in the alphabet (A-1, B-2, ... Z-26), 
# then add each number together

import time

def main():
    print("BREAKING NEWS: Numerologists claim that they can determine a person's entire personality based upon the \"numeric value\" of their name.")
    print("The numeracy is a super complex and secret algorithm which sums each letter's place in the alphabet.")
    print("Provide your data I mean name to see what the Numerologists have to say.\n")

    name = input("YOUR NAME: ")
    print()

    sum = 0
    for letter in name:
        sum += ord(letter.upper()) - ord("A") + 1
    
    print("The Numerologists determine...\n")

    time.sleep(3)

    print("They determined", sum)
    
    predictions = [
        "That means you will have a very prosperous future.",
        "That means your toe will be amputated at some point in time.",
        "I'm so sorry for your loss.",
        "That means you are very brave and couragous.",
        "That means you are a very curious individual.",
        "Good luck, you're gonna need it.",
        "The Numerologists no longer like you."
        "The Numerologists have deemed this the best number, however, they have not stated why."
        "The Numerologists have deemed this the worst number, however, they have not stated why."
        "That's a cool number."
    ]
    print(predictions[sum % len(predictions)])

if __name__ == "__main__":
    main()