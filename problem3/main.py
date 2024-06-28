def playing_domino(cards, deck):
    max_card = None
    for x in cards:
        if x[0] == deck[0] or x[1] == deck[0]:
            if max_card is None or max(x) > max(max_card):
                max_card = x
        elif x[0] == deck[1] or x[1] == deck[1]:
            if max_card is None or max(x) > max(max_card):
                max_card = x
    if max_card is not None:
        return max_card
    else:
        return []

if __name__ == "__main__":
    print(playing_domino([[6, 5], [3, 4], [2, 1], [3, 3]], [4, 3]))  # [3, 4]
    print(playing_domino([[6, 5], [3, 3], [3, 4], [2, 1]], [3, 6]))  # [6, 5]
    print(playing_domino([[6, 6], [2, 4], [3, 6]], [5, 1]))         # []