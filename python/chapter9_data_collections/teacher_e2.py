# Interactive List Algorithm Visualizer with Scoreboard

# ----- GLOBAL SCOREBOARD ----- #
scoreboard = {
    "count_runs": 0,
    "isin_runs": 0,
    "index_runs": 0,
    "reverse_runs": 0,
    "sort_runs": 0,
    "total_operations": 0
}

# ----- VISUALIZATION FUNCTION ----- #
def visualize(lst):
    print("List Visualization:")
    for val in lst:
        print(f"{val}: " + "#" * val)
    print()

# ----- ALGORITHMS ----- #
def count(lst, x):
    ops = 0
    ans = 0
    for item in lst:
        ops += 1
        print(f"Checking {item}...")
        if item == x:
            ans += 1
            print(f"Found {x}! Count is now {ans}")
    return ans, ops

def isin(lst, x):
    ops = 0
    for item in lst:
        ops += 1
        print(f"Checking {item}...")
        if item == x:
            print(f"{x} found!")
            return True, ops
    return False, ops

def index(lst, x):
    ops = 0
    for i in range(len(lst)):
        ops += 1
        print(f"Checking index {i}, value {lst[i]}...")
        if lst[i] == x:
            print(f"Found at index {i}")
            return i, ops
    return -1, ops

def reverse(lst):
    ops = 0
    print(f"Original list: {lst}")
    visualize(lst)

    for i in range(len(lst) // 2):
        j = -i - 1
        ops += 1
        print(f"Swapping {lst[i]} and {lst[j]}")
        lst[i], lst[j] = lst[j], lst[i]
        visualize(lst)
    
    return lst, ops

def sort(lst):
    ops = 0
    print(f"Original list: {lst}")
    visualize(lst)

    for i in range(len(lst) - 1):
        minpos = i
        for j in range(i + 1, len(lst)):
            ops += 1
            if lst[j] < lst[minpos]:
                minpos = j
        print(f"Swapping {lst[i]} with {lst[minpos]}")
        lst[i], lst[minpos] = lst[minpos], lst[i]
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
        print("\n--- Algorithm Visualizer ---")
        print("1. Count")
        print("2. Is In")
        print("3. Index")
        print("4. Reverse")
        print("5. Sort")
        print("6. Show Scoreboard")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            lst = get_list()
            x = int(input("Value to count: "))
            result, ops = count(lst, x)
            scoreboard["count_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Final count: {result} | Operations: {ops}")
        
        elif choice == "2":
            lst = get_list()
            x = int(input("Value to search: "))
            result, ops = isin(lst, x)
            scoreboard["isin_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Result: {result} | Operations: {ops}")
        
        elif choice == "3":
            lst = get_list()
            x = int(input("Value to find index: "))
            result, ops = index(lst, x)
            scoreboard["index_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Index: {result} | Operations: {ops}")
        
        elif choice == "4":
            lst = get_list()
            result, ops = reverse(lst)
            scoreboard["reverse_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Reversed list: {result} | Operations: {ops}")
        
        elif choice == "5":
            lst = get_list()
            result, ops = sort(lst)
            scoreboard["sort_runs"] += 1
            scoreboard["total_operations"] += ops
            print(f"Sorted list: {result} | Operations: {ops}")
        
        elif choice == "6":
            show_scoreboard()
        
        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()