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
    playerRandom = True  # randomize position
    cheat = True  # can see AI card
    otherPlayerAmount = 3  # number of AI
    cardNumMax = 10  # number of card per color
    initialCard = 7  # number of initial card in hand
    main(playerRandom, cheat, otherPlayerAmount, cardNumMax, initialCard)