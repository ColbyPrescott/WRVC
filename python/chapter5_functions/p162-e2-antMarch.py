def antMarch(numStr):
    return "The ants go marching " + numStr + " by " + numStr + ','

def printHurrah(numStr):
    print(antMarch(numStr) + " hurrah! hurrah!")

def printLittleOne(action):
    print("The little one stops to", action)

def printVerse(numStr, action):
    printHurrah(numStr)
    printHurrah(numStr)
    print(antMarch(numStr))
    printLittleOne(action)
    print("And they all go marching down...")
    print("In the ground...")
    print("To get out...")
    print("Of the rain.")
    print("Boom! Boom! Boom!")

def main():
    printVerse("one", "suck his thumb")
    printVerse("two", "tie his shoe")
    printVerse("three", "admire a bee")
    printVerse("four", "open a door")
    printVerse("five", "steal a dime")
    printVerse("six", "show a trick")
    printVerse("seven", "mess with Kevin")
    printVerse("eight", "break a gate")
    printVerse("nine", "do a crime")
    printVerse("ten", "go to bed")

main()