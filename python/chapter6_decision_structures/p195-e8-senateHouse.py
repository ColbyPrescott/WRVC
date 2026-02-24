# Write a program that calculated someone's eligibility for U.S. senator and representative
# Senator: At least 30 years old, been a citizen for at least 9 years
# Representative: At least 25 years old, been a citizen for at least 7 years

def main():
    age = int(input("Enter the person's age (years): "))
    citizenYears = int(input("Enter how long the person has been a U.S. citizen (years): "))

    if age >= 30 and citizenYears >= 9:
        print("Eligible for Senate")
    else:
        print("Not eligible for Senate")
    
    if age >= 25 and citizenYears >= 7:
        print("Eligible for House")
    else:
        print("Not eligible for House")

if __name__ == "__main__":
    main()