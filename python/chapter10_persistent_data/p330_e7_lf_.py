# LF is another made-up language
# In LF, the letters "lf" are added after the first vowel in a word, and then that vowel is repeated.
# The sentence "Don't talk in front of the kids" becomes "Dolfon't talfalk ilfin frolfront olfof thelfe kilfids."

from tkinter.filedialog import askopenfilename, asksaveasfilename

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

def translate_word_to_lf(word):
    """Take the word up to and including the first vowel, add "lf", then append the rest of the word including the first vowel"""
    i = first_vowel(word)
    lfword = word[:i+1] + "lf" + word[i:]
    return lfword

def translate_phrase_to_lf(phrase):
    """Split a phrase into each word, feed each word through the LF translator, then join the translated words back together with spaces.
    Also remove the last space, since nothing is appended afterward."""
    lfwords = ""
    for word in phrase.split():
        lfwords += translate_word_to_lf(word) + " "
    return lfwords[:-1]

def main():
    """Ask the user for the path of both the input and output file.
    Step through the input file line by line and feed each line into the LF line translator.
    For each tranlated line, write it to the output file."""
    print("Batch LF Translator")
    print("Choose file for input text")
    ifname = askopenfilename()
    print("Choose file to output the translated text")
    ofname = asksaveasfilename()
    with open(ifname, "r") as infile, open(ofname, "w") as outfile:
        for line in infile:
            print(translate_phrase_to_lf(line), file=outfile)
    print("Done")

if __name__ == "__main__":
    main()