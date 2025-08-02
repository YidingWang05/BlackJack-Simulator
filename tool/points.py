
def count_points(decks):
    points = 0
    for card in decks:
        if card[1] == "T" or card[1] == "J" or card[1] == "Q" or card[1] == "K":
            points += 10
        elif card[1] == "A" and points<=10:
            points += 11
        elif card[1] == "A" and points>10:
            points += 1
        else:
            points += int(card[1])
    return points

def is_blackjack(hands):
    if len(hands) == 2:
        if hands[0][1] == "A" and (hands[1][1] == "J" or hands[1][1] == "Q" or hands[1][1] == "K" or hands[1][1] == "T"):
            return True
        else:
            return False
    else:
        return False
