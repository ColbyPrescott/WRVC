# Body mass index is calculated as a person's weight (in pounds) times 703, divided by the square of the person's height (in inches).
# A BMI in the range of 19-25 (inclusive) is considered healthy.
# Write program to calculate to calculate BMI and print whether the person is above, within, or below healthy range

def main():
    weightPounds = float(input("Enter person's weight in pounds: "))
    heightInches = float(input("Enter person's height in inches: "))

    bmi = weightPounds * 703 / (heightInches * heightInches)
    print("BMI:", bmi)

    if bmi < 19:
        print("Person is below a healthy range. Ver thin, perhaps a stick")
    elif bmi <= 25:
        print("Person is in a healthy BMI range! Health™ says good job existing I guess")
    else:
        print("Person is above a healthy range. A lil rotund, ver precious")

main()