import sys
from tool.deck import prepare_cards
from blackjack.game import blackjack_game
import random

chips = 0
number_of_decks = 6 # classic casino numbers of decks for blackjack, but in later update, enable changes to match different styles
isTraditionalShoe = True #this is used to track if this game use a traditional card shoe.

while True:
    print("Welcome to the table.")
    playing = input("Do you want to play? (Press n to exit, any other letter key to continue) ")
    if playing == "n" or playing == "N":
        print("Player stops playing.")
        sys.exit(0) # stop the program

    while (chips < 5):
        buyIn = int(input("buy in new chips? (only integers of buy-in): £"))
        if buyIn <= 0: # check for zero or negative
            print("Sorry, buy-in can't be zero or negative.")
            continue

        chips = chips + buyIn

        if chips < 5:
            print("sorry, the minimum bet for this table is £5, unable to start game if you only have less than £5. ")
            print("The value of your current chips is: £" + str(chips))
            playing = input("Do you want to leave? (Press n to exit, any other letter key to buy more chips) ")
            if playing == "n" or playing == "N":
                print("Player stops playing.")
                sys.exit(0)
            continue

    is_trad = input("Do you want to use traditional card shoe? (Press Y/y for yes, any other key for modern auto-shaffle machine: ")
    if is_trad == "y" or is_trad == "Y":
        isTraditionalShoe = True
    else:
        isTraditionalShoe = False

    print("Your chips: £" + str(chips))
    decks = prepare_cards(number_of_decks)
    random_index = random.uniform(0.15, 0.25)
    # decks = ['CA','CQ','C3','CA','CQ','CA','CA','CA','CA','CK','C5']
    if isTraditionalShoe:
        last_card = int(random_index*len(decks))
    else:
        last_card = 0
    chips, decks = blackjack_game(chips, decks, last_card, number_of_decks)
    # print(decks, number_of_cards)



