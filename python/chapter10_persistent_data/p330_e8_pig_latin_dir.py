# Write a program to convert a sentence into Pig Latin, a made-up language.
# Translating a word to PL means moving its initial consonant cluster to the end fo the word and adding "ay."
# If the English word starts with a vowel, then "way" is appended to the word.
# Ex: "Don't talk in front of the kids" becomes "On'tday alktay inway ontfray ofway ethay idskay"
# To help write the program, structure it with
#   firstVowel(word) returns the index of the first vowel in word
#   translateWordToPL(word) returns the Pig Latin translation of a isngle word
#   trnaslatePhraseToPL(phrase) returns treanslation of a phrase
# For this program, treat "y" as a consonant if it is the first letter of a word and a vowel if it appears elsewhere

# Every .txt file in a directory

from tkinter.filedialog import askdirectory, asksaveasfilename
from pathlib import Path

def first_vowel(word):
    """Start at the first character and step forward until the character is a vowel.
    If the first character is the letter Y, skip it as it does not count as a vowel in this case.
    Once a vowel is found, return the index where it appears in the word."""
    start = 0
    if word[start].lower() == "y":
        start = 1
    for i in range(start, len(word)):
        if word[i] in "aeiouy":
            return i

def translate_word_to_pl(word):
    """If a word begins with a vowel, the pig latin translation is just the same word but with "way" appended to the end.
    Otherwise, the letters after the vowel are moved to the beginning, and "ay" is appended to the end.
    If the original word was uppercased, uppercase the translated word."""
    i = first_vowel(word)
    if i == 0:
        return word + "way"
    plword = word[i:] + word[:i].lower() + "ay"
    # Fix for if the first letter should be uppercase
    if word[0].upper() == word[0]:
        plword = plword[0].upper() + plword[1:]
    return plword

def translate_phrase_to_pl(phrase):
    """Split a phrase into each word, feed each word through the pig latin translator, then join the translated words back together with spaces.
    Also remove the last space, since nothing is appended afterward."""
    plphrase = ""
    for word in phrase.split():
        plphrase += translate_word_to_pl(word) + " "
    return plphrase[:-1]

def main():
    """Ask the user for the path of both the input and output file.
    Step through the input file line by line and feed each line into the pig latin line translator.
    For each tranlated line, write it to the output file."""
    print("Pig Latin Translator")
    print("Choose directory containing all .txt files to translate")
    indir = Path(askdirectory())
    print("Choose directory to output the .pgl translated files")
    outdir = Path(askdirectory())
    for ifname in indir.glob("*.txt"):
        with (open(ifname, "r") as infile, 
              open(outdir / ifname.with_suffix(".pgl").name, "w") as outfile):
            for line in infile:
                print(translate_phrase_to_pl(line), file=outfile)
    print("Done")

if __name__ == "__main__":
    main()