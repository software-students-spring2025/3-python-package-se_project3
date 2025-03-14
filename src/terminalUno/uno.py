import random
from enum import Enum
import time

class Color(Enum):
    RED = "Red"
    GREEN = "Green"
    BLUE = "Blue"
    YELLOW = "Yellow"
    BLACK = "Black"

class Type(Enum):
    NUMBER = "Number"
    SKIP = "Skip"
    REVERSE = "Reverse"
    DRAW2 = "Draw2"
    WILD = "Wild"
    WILD4 = "Wild4"

class Card:
    def __init__(self, color, type, number=None):
        self.color = color
        self.type = type
        self.number = number

    def __repr__(self):
        return f"{self.color.value} {self.type.value} {self.number if self.number is not None else ''}".strip()

class Deck():
    def __init__(self, cardNumMax = 10, initialCard = 7):
        self.cardNumMax = cardNumMax
        self.initialCard = initialCard
        self.cards = []
        self.initialize()


    def initialize(self):
        self.cards = []
        self.discard_pile = []
        colors = [Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW]
        for color in colors:
            self.cards.append(Card(color, Type.NUMBER, 0))
            for num in range(1, self.cardNumMax):
                self.cards.append(Card(color, Type.NUMBER, num))
                self.cards.append(Card(color, Type.NUMBER, num))
            self.cards.append(Card(color, Type.SKIP))
            self.cards.append(Card(color, Type.SKIP))
            self.cards.append(Card(color, Type.REVERSE))
            self.cards.append(Card(color, Type.REVERSE))
            self.cards.append(Card(color, Type.DRAW2))
            self.cards.append(Card(color, Type.DRAW2))
        for _ in range(4):
            self.cards.append(Card(Color.BLACK, Type.WILD))
            self.cards.append(Card(Color.BLACK, Type.WILD4))
        print("Deck initialized.")
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw(self):
        return self.cards.pop() if self.cards else None

    def __len__(self):
        return len(self.cards)
    
    def __contains__(self, card):
        return card in self.cards

class Player:
    def __init__(self, name, is_ai=False):
        self.name = name
        self.is_ai = is_ai
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def remove_card(self, index):
        return self.hand.pop(index)

    def __repr__(self):
        return f"{self.name}: {self.hand}"

def is_valid_play(selected_card, top_card, current_color):
    if selected_card.type in [Type.WILD, Type.WILD4]:
        return True
    if selected_card.color == current_color:
        return True
    if selected_card.type == Type.NUMBER and top_card.type == Type.NUMBER:
        if selected_card.number == top_card.number:
            return True
    if top_card.type != Type.NUMBER and selected_card.type == top_card.type:
        return True
    return False

def initialize_players(otherPlayerAmount, playerRandom):
    players = []
    for i in range (otherPlayerAmount):
        ai_player_name = "AI " + str(i+1)
        players.append(Player(ai_player_name, True))

    position = 0
    if playerRandom:
        position = random.randint(0,otherPlayerAmount)
        players.insert(position, Player("You"))
    else:
        players.insert(0, Player("You"))
    print("You are at position", position+1)
    return players, position

def initialize_deck_and_discard_pile(cardNumMax, initialCard, players):
    deck = Deck(cardNumMax,initialCard)
    discard_pile = []
    for _ in range(initialCard):
        for player in players:
            card = deck.draw()
            if card is not None:
                player.add_card(card)
            else:
                print("Deck is empty while dealing!")
                return
    initial_discard = deck.draw()
    while initial_discard is not None and initial_discard.type in [Type.WILD, Type.WILD4]:
        deck.cards.insert(0, initial_discard)
        deck.shuffle()
        initial_discard = deck.draw()
    if initial_discard is None:
        print("Deck ran out of cards to start the game!")
        return
    discard_pile.append(initial_discard)
    return deck, discard_pile


def main(playerRandom, cheat, otherPlayerAmount, cardNumMax = 10, initialCard = 7):
    players, position = initialize_players(otherPlayerAmount, playerRandom)
    num_players = len(players)
    deck, discard_pile = initialize_deck_and_discard_pile(cardNumMax, initialCard, players)


    
    current_color = discard_pile[-1].color if discard_pile[-1].type != Type.WILD else random.choice([Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW])
    
    current_player_index = 0
    direction = 1

    while True:
        player = players[current_player_index]
        print(f"\n*** {player.name}'s Turn ***")
        print(f"Current Card: {discard_pile[-1]}")
        if discard_pile[-1].type in [Type.WILD, Type.WILD4]:
            print(f"Current color: {current_color.value}")
        print("Other Players' Hands:", end=" ")
        for p in players:
            if p != player:
                if cheat and p.is_ai:
                    print(f"{p.name}: {p.hand}", end="  ")
                else:
                    print(f"{p.name}: {len(p.hand)} cards", end="  ")
        print("\n")

        if not player.is_ai:
            print("Your Hand:")
            for i, card in enumerate(player.hand):
                print(f"{i+1}: {card}")
            print("0: Draw a Card")
            while True:
                try:
                    choice = input("Choose a card to play (Enter number): ")
                    if not choice.isdigit():
                        print("Invalid input. Please enter a number.")
                        continue
                    choice = int(choice)
                    if choice == 0:
                        drawn_card = deck.draw()
                        if drawn_card is not None:
                            player.add_card(drawn_card)
                            print("You drew a card.")
                        else:
                            print("Deck is empty.")
                        break
                    if choice < 1 or choice > len(player.hand):
                        print("Invalid selection. Choose a valid card number.")
                        continue
                    selected_card = player.hand[choice - 1]
                    if is_valid_play(selected_card, discard_pile[-1], current_color):
                        player.remove_card(choice - 1)
                        discard_pile.append(selected_card)

                        #wild for player
                        if selected_card.type in [Type.WILD, Type.WILD4]:
                            new_color_input = input("Choose a new color (Red, Green, Blue, Yellow): ").strip().upper()
                            if new_color_input in ["RED", "GREEN", "BLUE", "YELLOW"]:
                                current_color = Color[new_color_input]
                            else:
                                print("Invalid color, system is randomizing one for you.")
                                current_color = random.choice([Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW])
                            print(f"You played {selected_card} and changed color to {current_color.value}.")
                            print("得胜已是定局")
                        
                        #reverse for player
                        elif selected_card.type == Type.REVERSE:
                            current_color = selected_card.color
                            direction=-direction
                            print(f"You played {selected_card} and direction is reversed.")

                        #draw2 for player
                        elif selected_card.type == Type.DRAW2:
                            current_color = selected_card.color
                            next_player=(current_player_index + direction) % num_players
                            drawn_card = deck.draw()
                            players[next_player].add_card(drawn_card)
                            drawn_card = deck.draw()
                            players[next_player].add_card(drawn_card)
                            print(f"You played {selected_card} and next player draws two cards.")
                        
                        #skip for player
                        elif selected_card == Type.SKIP:
                            current_color = selected_card.color
                            print(f"You played {selected_card} and next player is skipped.")
                            current_player_index = current_player_index + 1
                        #normal cards
                        else:
                            current_color = selected_card.color
                            print(f"You played {selected_card}.")
                        break
                    else:
                        print("Invalid card selection. Choose a valid card.")
                except ValueError:
                    print("Invalid input. Please enter a number.")
        else:
            valid_card_found = False
            for i, card in enumerate(player.hand):
                if is_valid_play(card, discard_pile[-1], current_color):
                    selected_card = player.hand.pop(i)
                    discard_pile.append(selected_card)
                    #wild for ai
                    if selected_card.type in [Type.WILD, Type.WILD4]:
                        new_color = random.choice([Color.RED, Color.GREEN, Color.BLUE, Color.YELLOW])
                        current_color = new_color
                        print(f"{player.name} played {selected_card} and changed color to {new_color.value}.")

                    #reverse for ai
                    elif selected_card.type == Type.REVERSE:
                        current_color = selected_card.color
                        direction=-direction
                        print(f"{player.name} played {selected_card} and and direction is reversed.")

                    #draw2 for ai
                    elif selected_card.type == Type.DRAW2:
                        current_color = selected_card.color
                        next_player=(current_player_index + direction) % num_players
                        drawn_card = deck.draw()
                        players[next_player].add_card(drawn_card)
                        drawn_card = deck.draw()
                        players[next_player].add_card(drawn_card)
                        print(f"{player.name} played {selected_card} and next player draws two cards.")
                    
                    #skip for ai
                    elif selected_card == Type.SKIP:
                            current_color = selected_card.color
                            print(f"{player.name} played {selected_card} and next player is skipped.")
                            current_player_index = current_player_index + 1

                    #noraml cards
                    else:
                        current_color = selected_card.color
                        print(f"{player.name} played {selected_card}.")
                    valid_card_found = True

                    break
            if not valid_card_found:
                drawn_card = deck.draw()
                if drawn_card:
                    player.add_card(drawn_card)
                    print(f"{player.name} drew a card.")
                else:
                    print("Deck is empty.")
        
        if not player.hand:
            print(f"{player.name} wins!")
            break

        current_player_index = (current_player_index + direction) % num_players
        for i in range (3):
            time.sleep(0.5)
            print("  @   ",end="")
            time.sleep(0.5)
        print("\n")
        
if __name__ == "__main__":
    playerRandom= True #randomize position
    cheat = True #can see AI card
    otherPlayerAmount = 1 #number of AI
    # cardNumMax = 3 #number of card per color
    # initialCard = 7 #numner of initial card in hand
    # main(playerRandom, cheat, otherPlayerAmount, cardNumMax, initialCard)
    main(playerRandom, cheat, otherPlayerAmount)