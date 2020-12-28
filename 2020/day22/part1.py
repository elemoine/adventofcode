import collections


def parse_cards(inputfile):
    with open(inputfile) as f:
        data = f.read()
    player1, player2 = data.split("\n\n")
    player1_deck = collections.deque()
    for line in player1.splitlines():
        try:
            v = int(line.strip())
        except Exception:
            v = None
        if v:
            player1_deck.appendleft(v)
    player2_deck = collections.deque()
    for line in player2.splitlines():
        try:
            v = int(line.strip())
        except Exception:
            v = None
        if v:
            player2_deck.appendleft(v)
    return player1_deck, player2_deck


def main():
    player1_deck, player2_deck = parse_cards("input")
    while player1_deck and player2_deck:
        card1 = player1_deck.pop()
        card2 = player2_deck.pop()
        if card1 > card2:
            player1_deck.extendleft([card1, card2])
        elif card2 > card1:
            player2_deck.extendleft([card2, card1])
        else:
            raise Exception("equal values")
    winner = player1_deck or player2_deck
    score = sum((i + 1) * card for i, card in enumerate(winner))
    print(score)


if __name__ == "__main__":
    main()
