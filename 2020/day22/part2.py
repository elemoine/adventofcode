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


def checksum(deck):
    sum(deck)


def play_game(deck1, deck2, previous_decks1, previous_decks2):
    while deck1 and deck2:
        key1 = tuple(deck1)
        key2 = tuple(deck2)
        if key1 in previous_decks1 and key2 in previous_decks2:
            return 1
        card1 = deck1.pop()
        card2 = deck2.pop()
        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = collections.deque(list(deck1)[len(deck1) - card1:])
            new_deck2 = collections.deque(list(deck2)[len(deck2) - card2:])
            round_winner = play_game(new_deck1, new_deck2, set(), set())
        else:
            round_winner = 1 if card1 > card2 else 2
        if round_winner == 1:
            deck1.extendleft([card1, card2])
        else:
            deck2.extendleft([card2, card1])
        previous_decks1.add(key1)
        previous_decks2.add(key2)
    assert not deck1 or not deck2
    return 1 if deck1 else 2


def main():
    player1_deck, player2_deck = parse_cards("input")
    winner = play_game(player1_deck, player2_deck, set(), set())
    winner_deck = player1_deck if winner == 1 else player2_deck
    score = sum((i + 1) * card for i, card in enumerate(winner_deck))
    print(score)


if __name__ == "__main__":
    main()
