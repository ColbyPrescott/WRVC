# Create a program that will infer a student's year in college based on how many credits they have
# Less than 7: Freshman
# At least 7 to be: Sophomore
# At least 16 to be: Junior
# At least 26 to be: Senior

def main():
    credits = int(input("Enter current number of credits: "))
    
    yearLabel = ""
    if credits < 0:
        yearLabel = "Error"
    elif credits < 7:
        yearLabel = "Freshman"
    elif credits < 16:
        yearLabel = "Sophomore"
    elif credits < 26:
        yearLabel = "Junior"
    else:
        yearLabel = "Senior"
    
    print("Student is currently:", yearLabel)

main()