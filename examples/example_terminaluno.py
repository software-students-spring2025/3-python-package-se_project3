import terminalUno.uno as uno
import time

def main():
    playerRandom = True  
    cheat = False 
    otherPlayerAmount = 1  
    cardNumMax = 10 
    initialCard = 7  

    # Initialize Players
    players = uno.initialize_players(otherPlayerAmount, playerRandom)
    num_players = len(players)
    print("Players initialized:", [player.name for player in players])

    # Initialize Deck and Discard Pile
    deck, discard_pile, current_color = uno.initialize_deck_and_discard_pile(cardNumMax, initialCard, players)
    print("Deck and discard pile initialized.")
    print(f"First card on the discard pile: {discard_pile[-1]} (Color: {current_color.value})")

    current_player_index = 0
    direction = 1
    game_over = False

    # Main uno game
    while not game_over:
        player = players[current_player_index]

        print(f"\nIt's {player.name}'s turn.")
        uno.display_game_state(player, players, discard_pile, current_color, cheat)

        # Handle player's turn
        current_color, direction, skip_flag, game_over = uno.handle_player_turn(
            player, players, deck, discard_pile, current_color, current_player_index, direction, cheat
        )

        if game_over:
            print(f"\n{player.name} has won!")
            break

        # Skip a player
        if skip_flag:
            print(f"{players[current_player_index].name} is skipped.")
            current_player_index = (current_player_index + direction * 2) % num_players
        else:
            current_player_index = (current_player_index + direction) % num_players

        for _ in range(3):
            time.sleep(0.5)
            print("  @   ", end="")
            time.sleep(0.5)
        print("\n")

        # Reshuffled the deck
        reshuffled = uno.check_and_refresh_deck(deck, discard_pile)

    print("\nGame Over!")

if __name__ == "__main__":
    main()