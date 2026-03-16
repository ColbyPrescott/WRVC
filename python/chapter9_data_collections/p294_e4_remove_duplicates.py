# Write and test a function removeDuplicates(somelist) that removes duplicate values from a list

def remove_duplicates(some_list):
    result = []
    for x in some_list:
        if not x in result:
            result.append(x)
    return result

def remove_duplicates_without_order(some_list):
    return list(set(some_list))

def main():
    test_arr = [9, 7, 1, 2, 3, 4, 2, 3, 5, 6, 1, 3, 9]
    print(remove_duplicates(test_arr))
    print(remove_duplicates_without_order(test_arr))

if __name__ == "__main__":
    main()