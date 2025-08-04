from tool.points import count_points
from tool.pairCheck import pair_check
from tool.bjCheck import is_blackjack
from tool.deck import prepare_cards

def blackjack_traditional (chips, decks, last_card, num_of_deck):
    if len(decks) >= num_of_deck*52:
        print("burning cards, draw 5 cards. ")
        for i in range(5):
            print("card " + str(i))
            decks.pop(0)
            # this is a burning cards rule, often used in traditional blackjack.
            # when this rule apply, when a new sets of cards first in use, need to draw some cards out without showing to anyone
            # typically, 3 to 10 cards. Each casino has their own rule.

    while True:
        # when the last card has been drawn, re-shuffle the decks
        if len(len(decks) < last_card):
            decks = prepare_cards(num_of_deck)
            print("Too less cards left")
            print("shuffling decks")
            print("burning cards, draw 5 cards. ")
            for i in range(5):
                print("card " + str(i))
                decks.pop(0)
            last_card = int(0.2*len(decks)) # mark the last card position.

        dealer = []
        player = [[0]]  # player's hand use 2D array, each hand in a list
        bets = []  # a list to track each hands' main bets.
        sides_bets = [[]]  # a 2D array to track sides bets, each list service one hand, inside this list, each element can stand for one bet, tie? pair? first3 cards?
        payout = 0
        print("your chips: £", chips)

        bet_down = int(input("place your bet: £"))
        if bet_down > chips:
            print("no sufficient chips available.")
            buy_in = input("entre the amount of chips you want, or press n to leave: £")
            if buy_in == 'n':
                break
            chips += int(buy_in)
            continue

        if bet_down < 5 or (bet_down % 5 != 0):
            print("Minimum bet £5, and the bets must be multiple of 5")
            continue
        player.append([])
        bets.append(bet_down)
        chips -= bets[0]

        num_of_hands = 1
        index = 0
        # use a while loop to ask if user want one more hand
        while True and (len(bets)) <= 6:
            input1 = input("press m for one more hand, press c to continue with current hand: ")
            if input1 == "m" or input1 == "M":
                # if user want to play another hand, append an empty list in player to store the cards
                bet_down = int(input("place your bet for this hand: £"))
                # chips vs bet check
                if bet_down < 5 or (bet_down % 5 != 0):
                    print("Minimum bet £5, and the bets must be multiple of 5")
                    continue
                if bet_down > chips:
                    print("no sufficient chips available.")
                    buy_in = input("entre the amount of chips you want, or press n to leave: £")
                    if buy_in == 'n':
                        break
                    chips += int(buy_in)
                    continue
                #check end
                num_of_hands += 1
                player.append([])
                player[0].append(0)
                bets.append(bet_down)
                index += 1
                chips -= bets[index]
                continue
            elif input1 == "c" or input1 == "C":
                print("No more bets")
                break
            else:
                print("Invalid input")
                continue

        # use for-loop to draw cards for each hands of player.
        # player's first card
        for i in range(1, len(player)):
            player[i].append(decks.pop(0))
            # print(player)
            player[0][i-1] = count_points(player[i])
            print("player's hand-", str(i), ": ",player[i])
            print("player's points-", str(i), ": ", player[0][i-1])

        """
        player.append([])
        player[1].append(decks.pop(0))
        player[0][0] = count_points(player[1])
        print("player's hand: ", player[1])
        print("player's points: ", player[0][0])
        """
        # dealer's first card
        dealer.append(decks.pop(0))
        dealer_points = count_points(dealer)
        print("dealer's hand: ", dealer)
        print("dealer's points: ", dealer_points)
        # player's second card
        for i in range(1, len(player)):
            player[i].append(decks.pop(0))
            # print(player)
            player[0][i-1] = count_points(player[i])
            print("player's hand-", str(i), ": ", player[i])
            print("player's points-", str(i), ": ", player[0][i-1])

        # ask for hit or stand, when > 21 (bust) auto stop by rule
        i = 1
        while i < len(player):
            while True and player[0][i-1] < 21:
                print("Hit or stand on hand-",str(i),"?")
                is_hit = input("(h for hit and s for stand): ")
                if is_hit == 's' or is_hit == 'S' :
                    break
                elif is_hit == 'h' or is_hit == 'H':
                    player[i].append(decks.pop(0))
                    player[0][i-1] = count_points(player[i])
                    print("player's hand-", str(i), ": ", player[i])
                    print("player's points-", str(i), ": ", player[0][i - 1])
                else:
                    print("invalid input")
                    continue
            if is_blackjack(player[i]) and (dealer_points != 10 or dealer_points != 11):
                print("Blackjack on hand", str(i), "!")
                payout += 1.5*bets[i-1]
                print("your payout on this hand: ", str(payout))
                chips += payout
                payout = 0
                player.pop(i)
                bets.pop(i)
                player[0].pop(i-1)
                continue # if player has blackjack on this hand and dealer has no chance to get blackjack i.e. first card is not 10 or 11, directly pay player at 3 to 2

            if player[0][i-1] > 21:
                print("too much for hand", str(i))
                print("you lose the bet for this hand")
                player.pop(i)
                player[0].pop(i-1) # if this hand bust, directly lose, take away chips and cards
                bets.pop(i-1)
                print(player) #DEBUG ONLY
                print(bets) #DEBUG ONLY
                continue
            i += 1

        if len(player) <= 1:
            print("all player's hand busted, house win.") #if player bust all their hands, no need to draw cards for the dealer
        else:
            # dealer keeps drawing till >= 17
            # todo: compare player's each hand against dealer
            while dealer_points < 17:
                dealer.append(decks.pop(0))
                dealer_points = count_points(dealer)
                print("dealer's hand: ", dealer)
                print("dealer's points: ", dealer_points)
            # dealer too much
            if dealer_points > 21:
                print("too much for dealer!")
                for i in range(len(bets)):
                    payout += 2*bets[i]
                chips += payout
                print("total payout: ", str(payout))
            # player win
            else:
                for i in range(1, len(player)):
                    if is_blackjack(dealer) and (player[0][i-1] != 21):
                        print("dealer has blackjack!")
                    elif dealer_points < player[0][i-1]:
                        print("hand", str(i), "win!")
                        payout += 2*bets[i-1]
                        # push
                    elif dealer_points == player[0][i-1] or (is_blackjack(dealer) and is_blackjack(player[i])):
                        print("hand", str(i), "push!")
                        payout += bets[i-1] #if is a tie, just return the bet
                    else:
                        print("dealer's win!")

                chips += payout
                print("total payout: ", str(payout))

            # ask for another round?
        print("your chips: ", chips)
        is_next = input("Do you want to play next round? (press n to quit, any other key to continue): ")
        if is_next == "n":
            break
        else:
            continue


    return chips, decks