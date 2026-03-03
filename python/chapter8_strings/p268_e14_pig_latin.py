# Write a program to convert a sentence into Pig Latin, a made-up language.
# Translating a word to PL means moving its initial consonant cluster to the end fo the word and adding "ay."
# If the English word starts with a vowel, then "way" is appended to the word.
# Ex: "Don't talk in front of the kids" becomes "On'tday alktay inway ontfray ofway ethay idskay"
# To help write the program, structure it with
#   firstVowel(word) returns the index of the first vowel in word
#   translateWordToPL(word) returns the Pig Latin translation of a isngle word
#   trnaslatePhraseToPL(phrase) returns treanslation of a phrase
# For this program, treat "y" as a consonant if it is the first letter of a word and a vowel if it appears elsewhere

def first_vowel(word):
    start = 0
    if word[start].lower() == "y":
        start = 1
    for i in range(start, len(word)):
        if word[i] in "aeiouy":
            return i

def translate_word_to_pl(word):
    i = first_vowel(word)
    if i == 0:
        return word + "way"
    plword = word[i:] + word[:i].lower() + "ay"
    # Fix for if the first letter should be uppercase
    if word[0].upper() == word[0]:
        plword = plword[0].upper() + plword[1:]
    return plword

def translate_phrase_to_pl(phrase):
    plphrase = ""
    for word in phrase.split():
        plphrase += translate_word_to_pl(word) + " "
    return plphrase[:-1]

def main():
    print("Pig Latin Translator")
    full_input = ""
    line = ""
    while line != "STOP":
        line = input("Enter a line: ")
        full_input += line
    plphrase = translate_phrase_to_pl(full_input)
    print("Translated:", plphrase)

if __name__ == "__main__":
    main()