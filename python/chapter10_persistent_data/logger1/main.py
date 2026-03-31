from pathlib import Path
this_dir = Path(__file__).resolve().parent

def add_entry():
    entry = input("Enter your log: ")

    # Prevent empty entries
    if entry.strip() == "":
        print("Entry cannot be empty.\n")
        return
    
    with open(this_dir / "log.txt", "a") as file:
        file.write(entry + "\n")
    
    print("Saved!\n")

def view_entries():
    print("\n--- Log Entries ---")

    try:
        with open(this_dir / "log.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No entries yet.")
            else:
                for line in lines:
                    print(line.strip())
    except FileNotFoundError:
        print("No log file found yet.")
    
    print()

def main():
    while True:
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()