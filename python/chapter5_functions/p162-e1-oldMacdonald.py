def dup(phrase):
    return phrase + ', ' + phrase

def aOrAn(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    if(any(word[0] == vowel for vowel in vowels)):
        return "an"
    else:
        return 'a'

def eieio():
    return dup("Ee-igh") + ", Oh!"

def macDonald():
    print("Old MacDonald had a farm,", eieio())

def verse(animal, sound):
    macDonald()
    print("And on that farm he had " + aOrAn(animal), animal + ',', eieio())
    print("With " + aOrAn(sound), dup(sound), "here and " + aOrAn(sound), dup(sound), "there.")
    print("Here " + aOrAn(sound), sound + ',', "there " + aOrAn(sound), sound + ',', "everywhere " + aOrAn(sound), dup(sound) + '.')
    macDonald()
    print()

def main():
    verse("cow", "moo")
    verse("pig", "oink")
    verse("chicken", "cluck")
    verse("horse", "neigh")
    verse("cat", "meow")
    verse("dog", "woof")
    verse("frog", "ribbit")
    verse("fox", "skreehya")
    verse("robot", "beep")
    verse("metal pipe", "clang")
    verse("nuclear reactor", "ominous noise")
    macDonald()

main()