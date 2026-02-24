# Write a program that accepts a quiz score from 0-5 and output
# 5-A, 4-B, 3-C, 2-D, 1-F, 0-F

def main():
    scoreNum = int(input("Score integer: "))
    
    scoreLetter = ''
    if scoreNum >= 5:
        scoreLetter = "A"
    elif scoreNum == 4:
        scoreLetter = "B"
    elif scoreNum == 3:
        scoreLetter = "C"
    elif scoreNum == 2:
        scoreLetter = "D"
    else:
        scoreLetter = "F"
    
    print("Score letter:", scoreLetter)

main()