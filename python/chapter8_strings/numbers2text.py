def main():
    print("Convert a list of space-separated Unicode numbers back into a message")
    
    nums = map(int, input("Enter the numbers: ").split())

    print("Decoded message: ", end="")
    for num in nums:
        print(chr(num), end="")
    
    print()

if __name__ == "__main__":
    main()