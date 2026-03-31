def main():
    fname = input("Enter filename: ")
    infile = open(fname, "r")
    data = infile.read()
    infile.close()
    print(data)

main()