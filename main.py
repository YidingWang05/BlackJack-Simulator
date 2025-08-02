import sys

chips = 0
decks = 6 # classic casino numbers of decks for blackjack, but in later update, enable changes to match different styles
isTraditionalShoe = True #this is used to track if this game use a traditional card shoe.

while True:
    print("Welcome to the table.")
    playing = input("Do you want to play? (Press n to exit, any other letter key to continue) ")
    if playing == "n" or playing == "N":
        sys.exit(0)

    while (chips < 5):
        buyIn = int(input("buy in new chips? (only integers of buy-in): £"))
        if buyIn == 0:
            print("Sorry, buy-in can't be zero.")
            continue

        chips = chips + buyIn
        if chips < 5:
            print("sorry, the minimum bet for this table is £5, unable to start game if you only have less than £5. ")
            print("The value of your current chips is: £" + str(chips))
            playing = input("Do you want to leave? (Press n to exit, any other letter key to buy more chips) ")
            if playing == "n" or playing == "N":
                sys.exit(0)
            continue

    print("Your chips: £" + str(chips))



print("Player stop playing.")