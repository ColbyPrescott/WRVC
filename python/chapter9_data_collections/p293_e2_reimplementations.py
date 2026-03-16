# Some languages do not have the flexible built-in list (array) opertations that Python has.
# Write an algorithm for each of the following Python operations and test your algorithm by coding it up in a suitable function
# Dor example, as a function, reverse(myList) should do the same sas myList.revers().
# You are not allowed to use the corresponding Python mehtod to implement your function

# count(myList, x) (like myList.count(x))
# isin(myList, x) (like x in myList)
# index(myList, x) (like myList.index(x))
# reverse(myList) (like myList.reverse())
# sort(myList) (like myList.sort())

def count(myList, x):
    num = 0
    for y in myList:
        if y == x:
            num += 1
    return num

def isin(myList, x):
    for y in myList:
        if y == x:
            return True
    return False

def index(myList, x):
    for i in range(len(myList)):
        if myList[i] == x:
            return i
    raise ValueError(str(x) + " is not in the list, silly")

# def reverse(myList):
#     original = myList.copy()
#     for i in range(len(myList)):
#         myList[len(myList) - 1 - i] = original[i]

def reverse(myList):
    for i in range(len(myList) // 2):
        j = -i - 1
        myList[i], myList[j] = myList[j], myList[i]

def sort(myList):
    # Bubble sort or something
    for i in range(len(myList)):
        for j in range(len(myList) - 1 - i):
            if myList[j] > myList[j + 1]:
                myList[j], myList[j + 1] = myList[j + 1], myList[j]

def main():
    test_arr = [3, 4, 1, 2, 3, 1, 6, 5, 1, 9]
    print("count")
    print(count(test_arr, 1))

    print("isin")
    print(isin(test_arr, 5))
    print(isin(test_arr, 10))

    print("index")
    print(index(test_arr, 2))
    # print(index(test_arr, 10))

    print("reverse")
    print(test_arr)
    reverse(test_arr)
    print(test_arr)

    print("sort")
    sort(test_arr)
    print(test_arr)

if __name__ == "__main__":
    main()
