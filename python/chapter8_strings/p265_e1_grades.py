# A certain CS professor gives 5-point quizzes that are ggraded on the scale
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F
# Write a program that accepts a quiz score as an input and prints out the corresponding grade.
# Use a string as a lookup table instead of a decision

def main():
    grade = int(input("Please input a grade (0-5): "))

    grade_letters = "FFDCBA"
    letter = grade_letters[grade]

    print("\nGrade:", letter)

if __name__ == "__main__":
    main()