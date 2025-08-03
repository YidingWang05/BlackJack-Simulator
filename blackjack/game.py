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
        player = [[0]]  # player's hand use 2D array, each hand in a list
        bets = []  # a list to track each hands' main bets.
        sides_bets = [[]]  # a 2D array to track sides bets, each list service one hand, inside this list, each element can stand for one bet, tie? pair? first3 cards?

        dealer_points = 0
        player_points = 0
        print("your chips: £", chips)
        bet_down = int(input("place your bet: £"))

        if bet_down > chips:
            print("no sufficient chips available.")
            buy_in = input("entre the amount of chips you want, or press n to leave: £")
            if buy_in == 'n':
                break
            chips += int(buy_in)
            continue

        if bet_down <= 5 or (bet_down % 5 != 0):
            print("Minimum bet £5, and the bets must be multiple of 5")
            continue

        bets.append(bet_down)
        chips -= bet_down

        # player's first card
        player.append([])
        player[1].append(decks.pop(0))
        player_points = count_points(player[1])
        print("player's hand: ", player[1])
        print("player's points: ", player_points)
        # dealer's first card
        dealer.append(decks.pop(0))
        dealer_points = count_points(dealer)
        print("dealer's hand: ", dealer)
        print("dealer's points: ", dealer_points)
        # player's second card
        player[1].append(decks.pop(0))
        player_points = count_points(player[1])
        print("player's hand: ", player[1])
        print("player's points: ", player_points)

        # ask for hit or stand, when > 21 (bust) auto stop by rule
        while True and player_points < 21:
            isHit = input("Hit or stand? (h for hit and s for stand): ")
            if isHit == 's' or isHit == 'S' :
                break
            elif isHit == 'h' or isHit == 'H':
                player[1].append(decks.pop(0))
                player_points = count_points(player[1])
                print("player's hand: ", player[1])
                print("player's points: ", player_points)
            else:
                print("invalid input")
                continue

        if player_points > 21: print("too much!")
        else:
            # dealer keeps drawing till >= 17
            while dealer_points < 17:
                dealer.append(decks.pop(0))
                dealer_points = count_points(dealer)
                print("dealer's hand: ", dealer)
                print("dealer's points: ", dealer_points)
            # dealer too much
            if dealer_points > 21:
                print("too much for dealer!")
                if player_points <= 21:
                    print("player win!")
                    chips += 2*bets.pop(0)
            # player win
            if dealer_points < player_points:
                print("player win!")
                chips += 2*bets.pop(0)
            # push
            elif dealer_points == player_points:
                print("push")
                chips += bets.pop(0)
            else:
                print("dealer's win!")

            # ask for another round?
            print("your chips: ", chips)
            isNext = input("Do you want to play next round? (press n to quit, any other key to continue): ")
            if isNext == "n":
                break
            else:
                continue


    return chips, decks