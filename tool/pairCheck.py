from tool.points import count_points
def pair_check (cards):
    if(len(cards) == 2) and (count_points(cards[0]) == count_points(cards[1])):
        return True
    return False