# Write a program that accepts a quiz score from 0-100 and output
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# < 60: F

def main():
    scoreNum = int(input("Score integer: "))
    
    scoreLetter = ''
    if scoreNum >= 90:
        scoreLetter = "A"
    elif scoreNum >= 80:
        scoreLetter = "B"
    elif scoreNum >= 70:
        scoreLetter = "C"
    elif scoreNum >= 60:
        scoreLetter = "D"
    else:
        scoreLetter = "F"
    
    print("Score letter:", scoreLetter)

main()