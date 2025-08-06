from tool.points import count_points

def is_blackjack(cards):
    if len(cards) == 2 and count_points(cards)==21:
        return True
    return False