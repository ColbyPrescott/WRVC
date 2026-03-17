# Interactive Duplicate Remover with Visualization + Scoreboard

# ----- GLOBAL SCOREBOARD ----- #
scoreboard = {
    "remove_v1_runs": 0,
    "remove_v2_runs": 0,
    "total_operations": 0
}

# ----- VISUALIZATION ----- #
def visualize(lst):
    print("List Visualization:")
    for val in lst:
        print(f"{val}: " + "#" * val)
    print()

# ----- VERSION 1 (LIST-BASED) ----- #
def removeDuplicates(lst):
    ops = 0
    lst2 = []

    print("\nStarting list:", lst)
    visualize(lst)

    while lst != []:
        item = lst.pop(0)
        ops += 1
        print(f"Removed {item} from original list")

        if item not in lst2:
            print(f"{item} is unique --> adding to new list")
            lst2.append(item)
        else:
            print(f"{item} is duplicate --> skipping")
        
        print("Current unique list:", lst2)
        visualize(lst2)
    
    lst.extend(lst2)

    print("\nFinal list (duplicates removed):", lst)

    return lst, ops

# ----- VERSION 2 (DICTIONARY-BASED) ----- #
def removeDuplicates2(lst):
    ops = 0
    seen = {}

    print("\nStarting list:", lst)
    visualize(lst)

    while lst != []:
        item = lst.pop()
        ops += 1
        print(f"Processing {item}")

        seen[item] = True
        print(f"Tracking {item} in dictionary")
    
    lst.extend(list(seen.keys()))

    print("\nFinal list (duplicates removed):", lst)
    visualize(lst)

    return lst, ops

# ----- HELPER FUNCTIONS ----- #
def get_list():
    user_input = input("Enter numbers separated by spaces: ")
    return [int(x) for x in user_input.split()]

def show_scoreboard():
    print("\n===== SCOREBOARD =====")
    for key, value in scoreboard.items():
        print(f"{key}: {value}")
    print("======================")

# ----- MAIN PROGRAM ----- #
def main():
    while True:
        print("\n--- Duplicate Remover Lab ---")
        print("1. Remove Duplicates (List Method)")
        print("2. Remove Duplicates (Dictionary Method)")
        print("3. Compare Both Methods")
        print("4. Show Scoreboard")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            lst = get_list()
            result, ops = removeDuplicates(lst)
            scoreboard["remove_v1_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Operations: {ops}")

        elif choice == "2":
            lst = get_list()
            result, ops = removeDuplicates2(lst)
            scoreboard["remove_v2_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Operations: {ops}")
        
        elif choice == "3":
            lst = get_list()

            print("\n--- Running List Method ---")
            lst_copy1 = lst.copy()
            _, ops1 = removeDuplicates(lst_copy1)

            print("\n --- Running Dictionary Method ---")
            lst_copy2 = lst.copy()
            _, ops2 = removeDuplicates2(lst_copy2)

            print("\n===== COMPARISON =====")
            print(f"List Method Operations: {ops1}")
            print(f"Dictionary Method Operations: {ops2}")

            if ops1 < ops2:
                print("List method was more efficient!")
            elif ops2 < ops1:
                print("Dictionary method was more efficient!")
            else:
                print("Both performed equally!")
            
        elif choice == "4":
            show_scoreboard()
        
        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
