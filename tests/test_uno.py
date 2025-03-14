import pytest
from terminalUno import Card, Color, Type, Deck, Player, is_valid_play, uno
# for now run "PYTHONPATH=src pytest tests/test_uno.py" to activate tests

class TestUno:

    def test_initialize_players(self):
         players = uno.initialize_players(2, True)[0]
         assert len(players) == 3, "the number of players when 2 players are initialized should be 2"
         print("Initialize players test passed")

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

    def test_sanity(self):
        expected = True
        actual = True
        assert expected == actual, "Test failed"
        print("Pytest is running as expected")
    
    def test_card_creation(self): 
        card = Card(Color.RED, Type.NUMBER, 5)
        assert card.color == Color.RED
        assert card.type == Type.NUMBER
        assert card.number == 5

    def test_card_representation(self): 
        card = Card(Color.BLUE, Type.SKIP)
        assert repr(card) == "Blue Skip"

    def test_deck_initialization(self):
        deck = Deck(3, 7) 
        assert len(deck.cards) == 52  

    def test_deck_shuffle(self):
        deck1 = Deck(3, 7)
        deck2 = Deck(3, 7)
        deck1.shuffle()
        assert deck1.cards != deck2.cards 

    def test_deck_draw(self):
        deck = Deck(3, 7)
        size = len(deck.cards)
        card = deck.draw()
        while card is not None:
            size -= 1
            assert len(deck.cards) == size
            card = deck.draw()

    def test_player_initialization(self):
        player = Player("Test Player")
        assert player.name == "Test Player"
        assert player.is_ai is False
        assert player.hand == []

    def test_player_add_card(self):
        player = Player("Test Player")
        card = Card(Color.RED, Type.NUMBER, 5)
        player.add_card(card)
        assert len(player.hand) == 1
        assert player.hand[0] == card

    def test_player_remove_card(self):
        player = Player("Test Player")
        card = Card(Color.BLUE, Type.NUMBER, 3)
        player.add_card(card)
        removed_card = player.remove_card(0)
        assert removed_card == card
        assert len(player.hand) == 0

    def test_valid_play_same_color(self):
        top_card = Card(Color.RED, Type.NUMBER, 5)
        selected_card = Card(Color.RED, Type.SKIP)
        assert is_valid_play(selected_card, top_card, Color.RED) is True

    def test_valid_play_same_number(self):
        top_card = Card(Color.GREEN, Type.NUMBER, 3)
        selected_card = Card(Color.RED, Type.NUMBER, 3)
        assert is_valid_play(selected_card, top_card, Color.RED) is True

    def test_valid_play_wild_card(self):
        top_card = Card(Color.BLUE, Type.NUMBER, 7)
        selected_card = Card(Color.BLACK, Type.WILD)
        assert is_valid_play(selected_card, top_card, Color.BLUE) is True

    def test_invalid_play(self):
        top_card = Card(Color.YELLOW, Type.NUMBER, 8)
        selected_card = Card(Color.BLUE, Type.NUMBER, 2)
        assert is_valid_play(selected_card, top_card, Color.YELLOW) is False
