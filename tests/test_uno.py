import pytest
from terminalUno import Card, Color, Type, Deck, Player, is_valid_play, uno
# for now run "PYTHONPATH=src pytest tests/test_uno.py" to activate tests

class TestUno:

    def test_sanity(self):
        expected = True
        actual = True
        assert expected == actual, "Test failed"
        print("Pytest is running as expected")
    
    def test_card_creation(self): 
        card = Card(Color.RED, Type.NUMBER, 5)
        assert card.color == Color.RED, f"Card color should be RED, not {card.color}"
        assert card.type == Type.NUMBER, f"Card type should be NUMBER, not {card.type}"
        assert card.number == 5, f"Card number should be 5, not {card.number}"
        print("Normal Card creation test passed")

    def test_card_representation(self): 
        card = Card(Color.BLUE, Type.SKIP)
        assert repr(card) == "Blue Skip", f"Card representation should be 'Blue Skip', not {repr(card)}"
        print("Special Card representation test passed")

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

    def test_initialize_players(self):
         players = uno.initialize_players(2, True)[0]
         assert len(players) == 3, f"the number of players when 2 AI players are initialized should be 3, not {len(players)}"
         print("Initialize players test passed")

    def test_initialize_deck(self):
         players = uno.initialize_players(2, True)[0]
         deck, discard_pile = uno.initialize_deck_and_discard_pile(cardNumMax = 10, initialCard = 7, players = players)
         right_length = 108 - 21 - 1
         assert len(deck) == right_length, f"the number of cards in the deck after initial draw should be 86, not {len(deck)}"
         print("Initialize deck test passed")
         assert len(discard_pile) == 1, f"the number of cards in the discard pile should be 1, not {len(discard_pile)}"
         print("Initialize discard pile test1 : only 1 card in the discard_pile passed")
         assert discard_pile[0] not in deck, f"the discard pile should not be in the deck"
         print("Initialize discard pile test2 : initial_discard not in deck passed")

    def test_valid_play_same_color(self):
        top_card = Card(Color.RED, Type.NUMBER, 5)
        selected_card = Card(Color.RED, Type.SKIP)
        assert is_valid_play(selected_card, top_card, Color.RED) is True, f"Same Color Test failed"

    def test_valid_play_same_number(self):
        top_card = Card(Color.GREEN, Type.NUMBER, 3)
        selected_card = Card(Color.RED, Type.NUMBER, 3)
        assert is_valid_play(selected_card, top_card, Color.RED) is True, f"Same Number Test failed"

    def test_valid_play_wild_card(self):
        top_card = Card(Color.BLUE, Type.NUMBER, 7)
        selected_card = Card(Color.BLACK, Type.WILD)
        assert is_valid_play(selected_card, top_card, Color.BLUE) is True, f"Wild Card Test failed"

    def test_invalid_play(self):
        top_card = Card(Color.YELLOW, Type.NUMBER, 8)
        selected_card = Card(Color.BLUE, Type.NUMBER, 2)
        assert is_valid_play(selected_card, top_card, Color.YELLOW) is False, f"Invalid Play Test failed"

    def test_skip_card(self):
        # Setup a game scenario with 3 players
        players = [Player("Player1"), Player("Player2"), Player("Player3")]
        deck = Deck(3, 7)  # Smaller deck for testing
        # Initial state
        current_player_index = 0
        direction = 1
        current_color = Color.RED

        target_card = Card(Color.RED, Type.SKIP)
        
        # Apply the effect
        current_color, direction, skip_next = uno.apply_card_effect(
            target_card, players[0], players, current_player_index, 
            direction, current_color, deck
        )
        
        # Check that skip_next is True
        assert skip_next == True, "Skip card should set skip_next to True"

        print("Skip card functionality test passed")

