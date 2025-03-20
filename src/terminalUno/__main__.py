"""
In Python packages, this file called __main__.py is run when the package is run
directly from command line, as opposed to importing it into another program.
"""

import terminalUno.uno as uno
import time


def main(playerRandom, cheat, otherPlayerAmount, cardNumMax = 10, initialCard = 7):
    players = uno.initialize_players(otherPlayerAmount, playerRandom)
    num_players = len(players)
    deck, discard_pile, current_color = uno.initialize_deck_and_discard_pile(cardNumMax, initialCard, players)
    
    current_player_index = 0
    direction = 1
    game_over = False

    while not game_over:
        player = players[current_player_index]
        
        # Handle the current player's turn
        current_color, direction, skip_flag, game_over = uno.handle_player_turn(
            player, players, deck, discard_pile, current_color, 
            current_player_index, direction, cheat
        )
        
        if not game_over:
            # Move to next player
            if not skip_flag:
                current_player_index = (current_player_index + direction) % num_players
            else: #already indexed with skip cards
                current_player_index = (current_player_index + direction*2) % num_players
                
            # Animation pause between turns
            for _ in range(3):
                time.sleep(0.5)
                print("  @   ", end="")
                time.sleep(0.5)
            print("\n")

if __name__ == "__main__":
    playerRandom = input("Randomize player position? (y/n): ")
    cheat = input("Cheat? (y/n): ")
    otherPlayerAmount = int(input("(Press Enter for default 3 AI player)Number of AI players: ") or 3)
    cardNumMax = int(input("(Press Enter for default 9)Max number for the digit on cards: ") or 9)
    cardNumMax += 1
    initialCard = int(input("(Press Enter for default 7)Number of initial card in hand: ") or 7)

    if playerRandom == "n" or playerRandom == "N":
        playerRandom = False
    else:
        playerRandom = True
    if cheat == "y" or cheat == "Y":
        cheat = True
    else:
        cheat = False
    if (otherPlayerAmount == 0):
        otherPlayerAmount = 3
    if (cardNumMax == 1):
        cardNumMax = 10
    if (initialCard == 0):
        initialCard = 7

    print ("\n")
    print ("Player Random: ", playerRandom, end = " ")
    print (", Cheat: ", cheat, end = " ")
    print (", Number of AI players: ", otherPlayerAmount)
    print ("Max number for the digit on cards: ", cardNumMax, end = " ")
    print (", Number of initial card in hand: ", initialCard, end = " ")
    print ("\n")
    main(playerRandom, cheat, otherPlayerAmount, cardNumMax, initialCard)