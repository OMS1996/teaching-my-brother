import random

# Mapping moves to integers for easy comparison
move_map = {0: "rock", 1: "scissors", 2: "paper"}
reverse_move_map = {v: k for k, v in move_map.items()}  # Reverse mapping for player input

def get_computer_move():
    "Get the computer's move."
    return random.choice(list(move_map.keys()))  # Randomly selecting a move for the computer.

def get_player_move():
    "Get the player's move."
    player_move = None
    while player_move not in reverse_move_map:  # Looping until the player enters a valid move.
        player_input = input("Enter your move (rock, paper, or scissors): ").lower()  # Getting the player's move and converting it to lowercase.

        if player_input in ["quit", "q", "exit", "e", "stop", "s"]:
            print("Thanks for playing!")
            exit()
        
        if player_input not in reverse_move_map:
            print("Invalid move. Please enter either 'rock', 'paper', or 'scissors'.")
        else:
            player_move = reverse_move_map[player_input]

    return player_move

def get_winner(player_move, computer_move):
    "Get the winner of the game."
    if player_move == computer_move:
        return "It's a tie!"
    elif (player_move == 0 and computer_move == 1) or \
         (player_move == 1 and computer_move == 2) or \
         (player_move == 2 and computer_move == 0):
        return "You win!"
    else:
        return "You lose!"
    
def play_game():
    "Play the game."
    
    # Getting the moves for both the player and the computer.
    player_move = get_player_move()  # Getting the player's move.
    computer_move = get_computer_move()  # Getting the computer's move.

    # Getting the winner of the game.
    winner = get_winner(player_move, computer_move) 
    
    # Printing the moves and the winner of the game.
    print(f"Player move: {move_map[player_move]}")  # The F-string is used to format the string and insert the player's move.
    print(f"Computer move: {move_map[computer_move]}")  # The F-string is used to format the string and insert the computer's move.
    print(winner)  # Printing the winner of the game.

def constant_gamming():
    "Play the game endlessly."
    print("Welcome to rock paper scissors!")

    game_counter = 1  # Setting the initial value of the game counter to 1.
    # Playing the game for the first time.
    play_game()

    while True:  # Looping indefinitely.
        is_play_again = input("Do you want to play again? (yes/no): ").lower()
        if is_play_again not in ["yes", "y", "ye"]:
            break
        else:
            print(f"Game #{game_counter}:")
            play_game()  # Playing the game.
            game_counter += 1
            print()  # Printing a blank line.

# Starting the game.
constant_gamming()  # Starting the game.
