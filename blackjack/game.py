from tool.points import count_points

def blackjack_traditional (chips, decks):

    print("burning cards, draw 5 cards. ")
    for i in range(5):
        decks.pop(0)
        # this is a burning cards rule, often used in traditional blackjack.
        # when this rule apply, when a new sets of cards first in use, need to draw some cards out without showing to anyone
        # typically, 3 to 10 cards. Each casino has their own rule.

    while True:
        dealer = []
        player = [[]]  # player's hand use 2D array, each hand in a list
        bets = []  # a list to track each hands' main bets.
        sides_bets = [[]]  # a 2D array to track sides bets, each list service one hand, inside this list, each element can stand for one bet, tie? pair? first3 cards?

        dealer_points = 0
        player_points = 0

        dealer.append(decks.pop(0))
        dealer_points = count_points(dealer)




    return chips, decks