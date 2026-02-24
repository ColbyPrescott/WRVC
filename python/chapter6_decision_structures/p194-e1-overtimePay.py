# Many companies pay time-and-a-half for any hours worked above 40 in a given week.
# Write a program to input the number of hours worked and the hourly rate 
# and calculate the total wages for the week

def main():
    hours = float(input("Number of hours worked throughout the week: "))
    payRate = float(input("Dollars earned per hour: "))

    totalPay = 0
    if hours < 40:
        totalPay = hours * payRate
    else:
        totalPay = 40 * payRate
        totalPay += (hours - 40) * 1.5 * payRate
    
    print("Final pay for the week:", totalPay)

main()