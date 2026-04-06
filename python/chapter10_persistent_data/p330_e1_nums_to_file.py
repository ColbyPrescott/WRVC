# Implement the writeNumsToFile function for our stats library as described in the chapter

def get_numbers_from_file(filename):
    data = []
    with open(filename, "r") as infile:
        for line in infile.readline():
            data.append(float(line))
    return data

def write_numbers_to_file(data, filename):
    with open(filename, "w") as outfile:
        for num in data:
            print(num, file=outfile)

def main():
    data = []
    print("<Enter> to stop.")
    while True:
        inp = input("Enter number: ")
        if inp == "":
            break
        else:
            data.append(float(inp))
    print()
    filename = input("Enter file name: ")
    write_numbers_to_file(data, filename)

if __name__ == "__main__":
    main()