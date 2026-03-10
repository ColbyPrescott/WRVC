# Ask the user how many test scores to enter. Store them in a list, then display the list, the highest score, and the lowerst score

def main():
    num_scores = int(input("Enter the number of scores to enter: "))

    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score #{i + 1}: "))
        scores.append(score)
    print()

    print("All scores:", scores)
    print()
    print("Minimum:", min(scores))
    print("Maximum:", max(scores))

if __name__ == "__main__":
    main()