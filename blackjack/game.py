from tool.points import count_points
from tool.pairCheck import pair_check
from tool.bjCheck import is_blackjack
from tool.deck import prepare_cards
import os

# define a clear function
clear = lambda: os.system('cls')

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
        if len(decks) < last_card:
            decks = prepare_cards(num_of_deck)
            print("Too less cards left")
            print("shuffling decks")
            print("burning cards, draw 5 cards. ")
            for i in range(5):
                print("card " + str(i))
                decks.pop(0)
            last_card = int(0.2*len(decks)) # mark the last card position.

        dealer = []
        player_hand = [] # use following structure to store player hands' info [{"cards": [], "point": int, "hand_id": int, "split_id": int, "bet": double, "side_bets": [], }....]
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
        """player.append([])
        bets.append(bet_down)
        chips -= bets[0]"""

        hand = {"cards": [], "point": 0, "hand_id": 1, "split_id": 1, "bet": bet_down, "side_bets": []}
        chips -= bet_down
        player_hand.append(hand)

        index = 0
        # use a while loop to ask if user want one more hand
        while True and (len(player_hand)) < 6:
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
                index += 1
                hand = {"cards": [], "point": 0, "hand_id": index+1, "split_id": 1, "bet": bet_down, "side_bets": []}
                player_hand.append(hand)
                chips -= player_hand[index]["bet"]
                continue
            elif input1 == "c" or input1 == "C":
                print("No more bets")
                break
            else:
                print("Invalid input")
                continue
        # print(decks)
        # use for-loop to draw cards for each hands of player.
        # player's first card
        for i in range(0, len(player_hand)):
            player_hand[i]["cards"].append(decks.pop(0))
            player_hand[i]["point"] = count_points(player_hand[i]["cards"])
            print("player's hand-", str(i), ": ", player_hand[i]["cards"])
            print("player's points-", str(i), ": ", player_hand[i]["point"])

        # dealer's first card
        dealer.append(decks.pop(0))
        dealer_points = count_points(dealer)
        print("dealer's hand: ", dealer)
        print("dealer's points: ", dealer_points)
        # player's second card
        for i in range(0, len(player_hand)):
            player_hand[i]["cards"].append(decks.pop(0))
            player_hand[i]["point"] = count_points(player_hand[i]["cards"])
            print("player's hand-", str(i), ": ", player_hand[i]["cards"])
            print("player's points-", str(i), ": ", player_hand[i]["point"])
        # print(player_hand)
        # ask for hit or stand, when > 21 (bust) auto stop by rule
        # use a loop, iterate through all hands
        i = 0
        while i < len(player_hand):

            while True and player_hand[i]["point"] < 21:
                #  clear()
                # show hand
                print("Player hand-"+
                      str(player_hand[i]["hand_id"]) + "-"
                      + str(player_hand[i]["split_id"])
                      + str(player_hand[i]["cards"]))
                # show bets
                print("your bets on this hand: £" + str(player_hand[i]["bet"]))
                # if player's hand only have two cards, ask them if they want to double or split
                if len(player_hand[i]["cards"]) == 2:
                    print("your chips £", chips)
                    print("d for double")
                    print("x for split")
                    # choice = input("your choice: ")
                    # double
                # to be optimized, one possible solution is that when len(player[i]) == 2, print the guidance of double or split. When user input something lead to double and split, check if
                # len(player[i]) == 2. if so, proceed with command otherwise go to print("invalid")
                print("h for hit and s for stand, hand-",str(i),"?")
                choice = input("your choice: ")
                if (choice == 'd' or choice == 'D') and len(player_hand[i]["cards"]) == 2:
                    if chips >= player_hand[i]["bet"]:
                        chips -= player_hand[i]["bet"]
                        player_hand[i]["bet"] = player_hand[i]["bet"] * 2
                        player_hand[i]["cards"].append(decks.pop(0))
                        player_hand[i]["point"] = count_points(player_hand[i]["cards"])
                        print("player's hand-" + str(i), ": ", player_hand[i]["cards"])
                        break
                    else:
                        print("no sufficient chips available.")
                        print("To double or split, you must put the same amount of chips of your main bet for this hand")
                        is_buy_in = input("entre the amount of chips you want, or press n to quit: ")
                        if is_buy_in == 'n':
                            continue
                        else:
                            chips += int(is_buy_in)
                            print("your chips: £", chips)
                            continue
                elif (choice == 'x' or choice == 'X') and len(player_hand[i]["cards"]) == 2 and count_points(player_hand[i]["cards"][0]) == count_points(player_hand[i]["cards"][1]):
                    hand_id = player_hand[i]["hand_id"]
                    init_hand = [hands for hands in player_hand if hands["hand_id"] == hand_id]
                    split_id = init_hand[len(init_hand) - 1]["split_id"]
                    # print(init_hand)
                    print("player's hand-", str(i), ": ", init_hand[0]["cards"])
                    if len(init_hand) >= 4:
                        print("Can not split same hand over 4 times")
                        continue
                    if chips >= player_hand[i]["bet"]:
                        chips -= player_hand[i]["bet"]

                        new_hand = {
                            "cards": [player_hand[i]["cards"].pop(0)],
                            "point": player_hand[i]["point"],
                            "hand_id": player_hand[i]["hand_id"],
                            "split_id": split_id + 1,
                            "bet": bet_down,
                            "side_bets": []
                            }

                        player_hand[i]["cards"].append(decks.pop(0))
                        new_hand["cards"].append(decks.pop(0))
                        new_hand["point"] = count_points(new_hand["cards"])
                        player_hand.insert(i+len(init_hand), new_hand)
                        print(player_hand)
                        continue
                    else:
                        print("no sufficient chips available.")
                        print("To double or split, you must put the same amount of chips of your main bet for this hand")
                        is_buy_in = input("entre the amount of chips you want, or press n to quit: ")
                        if is_buy_in == 'n':
                            continue
                        else:
                            chips += int(is_buy_in)
                            print("your chips: £", chips)
                            continue


                elif choice == 's' or choice == 'S' :
                    print("player's hand-" + str(i + 1) + ": ", player_hand[i]["cards"])
                    print("player's points-" + str(i + 1) + ": ", player_hand[i]["point"])
                    break
                elif choice == 'h' or choice == 'H':
                    player_hand[i]["cards"].append(decks.pop(0))
                    player_hand[i]["point"] = count_points(player_hand[i]["cards"])
                    print("player's hand-" + str(i+1) + ": ", player_hand[i]["cards"])
                    print("player's points-" + str(i+1) + ": ",player_hand[i]["point"])
                else:
                    print("invalid input")
                    continue
            # blackjack check
            if is_blackjack(player_hand[i]["cards"]) and (dealer_points != 10 or dealer_points != 11):
                print("Blackjack on hand", str(i), "!")
                payout += 1.5*player_hand[i]["bet"]
                print("your payout on this hand: ", str(payout))
                chips += payout
                payout = 0
                player_hand.pop(i)
                continue # if player has blackjack on this hand and dealer has no chance to get blackjack i.e. first card is not 10 or 11, directly pay player at 3 to 2

            # bust check
            if player_hand[i]["point"] > 21:
                print("too much for hand", str(i))
                print("you lose the bet for this hand")
                player_hand.pop(i)
                # print(player_hand)
                continue
            i += 1

        if len(player_hand) < 1:
            print("all player's hand busted, house win.") #if player bust all their hands, no need to draw cards for the dealer
        else:
            # dealer keeps drawing till >= 17
            while dealer_points < 17:
                dealer.append(decks.pop(0))
                dealer_points = count_points(dealer)
                print("dealer's hand: ", dealer)
                print("dealer's points: ", dealer_points)
            # dealer bust
            if dealer_points > 21:
                print("too much for dealer!")
                for i in range(len(player_hand)):
                    payout += 2*player_hand[i]["bet"]
                chips += payout
                print("total payout: ", str(payout))
            # payout
            else:
                # compare player's each hand against dealers
                for i in range(1, len(player_hand)):
                    if is_blackjack(dealer) and not (is_blackjack(player_hand[i]["cards"])):
                        print("dealer has blackjack!")
                    elif dealer_points < player_hand[i]["point"]:
                        print("hand", str(i), "win!")
                        payout += 2*player_hand[i]["bet"]
                        # push
                    elif dealer_points == player_hand[i]["point"] or (is_blackjack(dealer) and is_blackjack(player_hand[i]["bet"])):
                        print("hand", str(i), "push!")
                        payout += player_hand[i]["bet"] #if is a tie, just return the bet
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