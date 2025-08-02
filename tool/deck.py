import itertools
import random

def prepare_cards ( number_of_decks ):
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    single_decks = [f"{suit}{rank}" for suit, rank in itertools.product(suits, ranks)]
    # print(single_decks)
    decks = single_decks * number_of_decks
    # print(decks)
    # print(len(decks))
    random.shuffle( decks )
    # print(decks)
    return decks
# d = prepare_cards(6)