
def count_points(decks):
    points = 0
    aces = 0
    for card in decks:
        if card[1] == "T" or card[1] == "J" or card[1] == "Q" or card[1] == "K":
            points += 10
        elif card[1] == "A":
            points += 11
            aces += 1 # mark how many aces we have
        else:
            points += int(card[1])
            """treat aces as 11 initially. If the points go over 21, we sub 10 from the total point.
                this action is equivalent to change aces to 1
            """
    while aces > 0 and points > 21 : # only aces can be changed from 11 to 1, therefore, the times of sub 10 can't exceed 21
        points -= 10
        aces -= 1
    return points



def is_blackjack(hands):
    if len(hands) == 2:
        if hands[0][1] == "A" and (hands[1][1] == "J" or hands[1][1] == "Q" or hands[1][1] == "K" or hands[1][1] == "T"):
            return True
        else:
            return False
    else:
        return False
