# Write and test a function to meet this specification:
# toNumbers(strList) strList is a list of strings, each of which represents a number. Modofy each entry in the list by converting it to a number

def toNumbers(strList):
    for i in range(len(strList)):
        strList[i] = float(strList[i])

def main():
    test = [1, 2, 3, 4, 5]
    toNumbers(test)
    print(test)

if __name__ == "__main__":
    main()