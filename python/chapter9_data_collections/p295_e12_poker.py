# Using the card representation proposed in the previous problem (rank, suit_char), write a set of functions that can be used to categorize five-card poker hands
# Straight flush: Five ranks in a row, all of the same suit
# Four of a kind: Four of the same rank
# Full house: Three of one rank and two of another
# Flush: Five cards of the same suit
# Straight Five ranks in a row
# Three of a kind: Three of one rank (but not a full house or four of a kind)
# Two pari: Two each of two different ranks
# Pair: Two of the same rank (but not two pair, three or four of a kind)

def unique_max_ranks(cards, unique_ranks, target_max_count):
    """Check if a hand has unqiue_ranks number of unique ranks and if the highest count of a rank is target_count"""
    if len(cards) != 5:
        raise Exception("Hand must have 5 cards")
    ranks = {}
    for card in cards:
        ranks.setdefault(card[0], 0)
        ranks[card[0]] += 1
    if len(ranks.keys()) != unique_ranks:
        return False
    max_count = max(ranks.values())
    return max_count == target_max_count

# Five ranks in a row, all of the same suit
def straight_flush(cards):
    return straight(cards) and flush(cards)

# Four of the same rank
def four_of_a_kind(cards):
    return unique_max_ranks(cards, 2, 4)

# Three of one rank and two of another
def full_house(cards):
    return unique_max_ranks(cards, 2, 3)

# Five cards of the same suit
def flush(cards):
    if len(cards) != 5:
        raise Exception("Hand must have 5 cards")
    suit = cards[0][1]
    return all(map(lambda card: card[1] == suit, cards))

# Five ranks in a row
def straight(cards):
    if len(cards) != 5:
        raise Exception("Hand must have 5 cards")
    sorted_cards = sorted(cards)
    for i in range(1, len(sorted_cards)):
        if sorted_cards[i][0] != sorted_cards[i - 1][0] + 1:
            return False
    return True

# Three of one rank (but not a full house or four of a kind)
def three_of_a_kind(cards):
    return unique_max_ranks(cards, 3, 3)

# Two each of two different ranks
def two_pair(cards):
    return unique_max_ranks(cards, 3, 2)

# Two of the same rank (but not two pair, three or four pair)
def pair(cards):
    return unique_max_ranks(cards, 4, 2)

def main():
    print("This program will classify a list of cards as poker hands.\n")

    cards = []
    for _ in range(5):
        inp = input("Enter card details (<rank 2-14> <suit letter>): ")
        rank, suit = inp.split()
        cards.append((int(rank), suit))
    
    print()
    print("Straight flush:", straight_flush(cards))
    print("Four of a kind:", four_of_a_kind(cards))
    print("Full house:", full_house(cards))
    print("Flush:", flush(cards))
    print("Straight:", straight(cards))
    print("Three of a kind:", three_of_a_kind(cards))
    print("Two pair:", two_pair(cards))
    print("Pair:", pair(cards))

if __name__ == "__main__":
    main()