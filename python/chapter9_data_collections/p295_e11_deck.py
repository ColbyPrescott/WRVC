# A playing card consists of a rank and a suit
# It can be represented as a touble of (rank, suit) where rank is an int and suit is a single-character string. 
# If aces are considered the highest card, it's convenient to use 2-14 to represent the ranks 2-10, jack, queen, king, ace
# So (2, "c") is the two of clubs, and (14, "s") is the ace of spades
# Write a function, makeDeck() that produces a list of 52 tuples representing a deck of cards

def make_deck():
    deck = []
    ranks = range(2, 15)
    suits = ["h", "d", "c", "s"] # Heart, diamond, club, spade
    for rank in ranks:
        for suit in suits:
            deck.append((rank, suit))
    return deck

def main():
    print("This program will generate a deck of 52 playing cards")

    print(make_deck())

if __name__ == "__main__":
    main()