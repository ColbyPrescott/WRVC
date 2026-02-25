# certain CS professor gives 100-point exams that are graded on the scale 
# 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F
# Write a program that accepts an exam score as input and prints out the correspoinding grade.
# Use a string lookup table instead of a decision

def main():
    grade = int(input("Please input a grade (0-100): "))

    grade_letters = "FFFFFFDCBAA"

    letter = grade_letters[grade // 10]

    print("Grade:", letter)

if __name__ == "__main__":
    main()