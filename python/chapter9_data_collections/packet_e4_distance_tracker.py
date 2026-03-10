# A runner records miles run each day for 7 days. 
# Calculate the total miles, average miles per day, and the longest single run

def main():
    print("Enter the miles run for each day")

    days = 7
    miles_for_day = []
    for i in range(days):
        miles = float(input(f"Miles in day #{i + 1}: "))
        miles_for_day.append(miles)
    
    total = sum(miles_for_day)
    avg = total / days
    longest = max(miles_for_day)

    print(f"Total: {total:.2f} mi")
    print(f"Average: {avg:.2f} mi")
    print(f"Longest run: {longest:.2f} mi")

if __name__ == "__main__":
    main()