inventory = {}
name = ""

def room1():
    print("You see a boring room.")
    choices = [
        ("Be sad", None),
        ("Be happy", None),
        ("Explore", None)
    ]

def intro():
    print("----- ADVENTURE THING -----")
    print()
    name = input("Enter your name: ")
    print()

room = room1
choices = []

def main():
    intro()

    room()
    choice = int(input("Enter your choice: "))

if __name__ == "__main__":
    main()

