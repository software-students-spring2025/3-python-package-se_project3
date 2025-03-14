import pytest
from terminalUno import uno

class TestUno:

    def test_sanity(self):
        excepted = True
        actual = True
        assert excepted == actual, "Test failed"
        print("Pytest is running as expected")
    
    # initialize_players
    def test_initialize_players(self):
        players = uno.initialize_players(2, True)[0]
        assert len(players) == 3, "the number of players when 2 players are initialized should be 2"
        print("Initialize players test passed")
    
    # initialize_deck_and_discard_pile
    def test_initialize_deck(self):
        players = uno.initialize_players(2, True)[0]
        deck, discard_pile = uno.initialize_deck_and_discard_pile(cardNumMax = 10, initialCard = 7, players = players)
        right_length = 108 - 21 - 1
        assert len(deck) == right_length, "the number of cards in the deck should be 108"
        print("Initialize deck test passed")
        assert len(discard_pile) == 1, "the number of cards in the discard pile should be 1"
        print("Initialize discard pile test1 : only 1 card in the discard_pile passed")
        assert discard_pile[0] not in deck, "the discard pile should not be in the deck"
        print("Initialize discard pile test2 : initial_discard not in deck passed")