import random

player_move, computer_move = None, None # Setting the initial values of the player and computer moves to None.
move_list = ["rock", "paper", "scissors"] # The set of moves that the player and computer can make.

def get_computer_move():
    "Get the computer's move."
    return random.choice(move_list) # Randomly selecting a move for the computer.

def get_player_move():
    "Get the player's move."
    player_move = None
    while player_move not in move_list: # Looping until the player enters a valid move.
        player_move = input("Enter your move (rock, paper, or scissors): ").lower() # Getting the player's move and converting it to lowercase.

        # Giving him the valid moves.
        if player_move not in move_list:
            print("Invalid move. Please enter either 'rock', 'paper', or 'scissors'\n. However, If you want to quit, type 'quit', 'q', 'exit', 'e', 'stop', or 's'.")
        
        if player_move == "quit" or player_move == "q" or player_move == "exit" or player_move == "e" or player_move == "stop" or player_move == "s":
            print("Thanks for playing!")
            exit()

    return player_move

def get_winner(player_move, computer_move):
    "Get the winner of the game."
    if player_move == computer_move: # If the player and computer make the same move, it's a tie.
        return "It's a tie!"
    elif player_move == "rock" and computer_move == "scissors": # If the player chooses rock and the computer chooses scissors, the player wins.
        return "You win!"
    elif player_move == "paper" and computer_move == "rock": # If the player chooses paper and the computer chooses rock, the player wins.
        return "You win!"
    elif player_move == "scissors" and computer_move == "paper": # If the player chooses scissors and the computer chooses paper, the player wins.
        return "You win!"
    else: # If none of the above conditions are met, the computer wins.
        return "You lose!"
    
def play_game():
    "Play the game."
    
    # Getting the moves for both the player and the computer.
    player_move = get_player_move() # Getting the player's move."
    computer_move = get_computer_move() # Getting the computer's move.

    # Getting the winner of the game.
    winner = get_winner(player_move, computer_move) 

    
    # Printing the moves and the winner of the game.
    print(f"Player move: {player_move}") # The F-string is used to format the string and insert the player's move.
    print(f"Computer move: {computer_move}") #  The F-string is used to format the string and insert the computer's move.
    print(winner) # Printing the winner of the game.


def constant_gamming():
    "Play the game endlessly."
    print("Welcome to rock paper scissors!")

    game_counter = 0 # Setting the initial value of the game counter to
    # Playing the game for the first time.
    play_game()

    while True: # Looping indefinitely.
        is_play_again = input("Do you want to play again? (yes/no): ").lower()
        if  is_play_again != "yes" or is_play_again != "y" or is_play_again != "ye":
            break
        else:
            game_counter += 1
            print(f"Game #{game_counter}:")
            play_game() # Playing the game.
            print() # Printing a blank line.

# Starting the game.
constant_gamming() # Starting the game.



