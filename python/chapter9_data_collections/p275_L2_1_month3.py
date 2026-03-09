def main():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    
    n = int(input("Enter a month number (1-12): "))

    print(f"The month abbreviation is {months[n - 1]}.")

if __name__ == "__main__":
    main()