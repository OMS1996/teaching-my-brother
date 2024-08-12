import random

class RockPaperScissorsGame:
    def __init__(self):
        self.move_map = {0: "rock", 1: "scissors", 2: "paper"}
        self.reverse_move_map = {v: k for k, v in self.move_map.items()}
        self.game_counter = 0
        self.history = []  # To store the history of games

    def get_computer_move(self):
        "Get the computer's move."
        return random.choice(list(self.move_map.keys()))

    def get_player_move(self):
        "Get the player's move."
        player_move = None
        while player_move not in self.reverse_move_map:  # Looping until the player enters a valid move.
            player_input = input("Enter your move (rock, paper, or scissors): ").lower()  # Getting the player's move and converting it to lowercase.

            if player_input in ["quit", "q", "exit", "e", "stop", "s"]:
                print("Thanks for playing!")
                exit()
            
            if player_input not in self.reverse_move_map:
                print("Invalid move. Please enter either 'rock', 'paper', or 'scissors'.")
            else:
                player_move = self.reverse_move_map[player_input]

        return player_move

    def get_winner(self, player_move, computer_move):
        "Get the winner of the game."
        if player_move == computer_move:
            return "It's a tie!"
        elif (player_move == 0 and computer_move == 1) or \
             (player_move == 1 and computer_move == 2) or \
             (player_move == 2 and computer_move == 0):
            return "You win!"
        else:
            return "You lose!"

    def play_game(self):
        "Play a single game and record the result."
        self.game_counter += 1
        
        player_move = self.get_player_move()  # Getting the player's move
        computer_move = self.get_computer_move()  # Getting the computer's move
        winner = self.get_winner(player_move, computer_move)  # Determining the winner

        # Record the game result in history
        game_result = {
            "Game #": self.game_counter,
            "Player Move": self.move_map[player_move],
            "Computer Move": self.move_map[computer_move],
            "Result": winner
        }
        self.history.append(game_result)

        # Print the moves and the winner of the game
        print(f"Player move: {self.move_map[player_move]}")
        print(f"Computer move: {self.move_map[computer_move]}")
        print(winner)

    def display_history(self):
        "Display the history of games played."
        if not self.history:
            print("No games played yet.")
        else:
            for game in self.history:
                print(game)

    def start(self):
        "Start the game loop."
        print("Welcome to rock paper scissors!")
        
        self.play_game()  # Play the first game

        while True:  # Loop indefinitely to allow replaying
            is_play_again = input("Do you want to play again? (yes/no): ").lower()
            if is_play_again not in ["yes", "y", "ye"]:
                break
            else:
                print(f"Game #{self.game_counter + 1}:")
                self.play_game()
                print()  # Print a blank line

        # After exiting, show the game history
        print("\nGame history:")
        self.display_history()

# Create a game instance and start the game
game = RockPaperScissorsGame()
game.start()
