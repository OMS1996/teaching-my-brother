import random
import tkinter as tk
from tkinter import messagebox

class RockPaperScissorsGame:
    def __init__(self):
        self.move_map = {0: "rock", 1: "scissors", 2: "paper"}
        self.reverse_move_map = {v: k for k, v in self.move_map.items()}
        self.game_counter = 0
        self.history = []  # To store the history of games
        
        self.create_gui()

    def create_gui(self):
        self.root = tk.Tk()
        self.root.title("Rock Paper Scissors")

        # Label to display game instructions
        self.label = tk.Label(self.root, text="Choose your move:")
        self.label.pack()

        # Buttons for Rock, Paper, Scissors
        self.rock_button = tk.Button(self.root, text="Rock", command=self.player_chose_rock)
        self.rock_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.paper_button = tk.Button(self.root, text="Paper", command=self.player_chose_paper)
        self.paper_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.scissors_button = tk.Button(self.root, text="Scissors", command=self.player_chose_scissors)
        self.scissors_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Text widget to display game history
        self.history_text = tk.Text(self.root, height=10, width=50)
        self.history_text.pack(pady=10)

        # Quit button
        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.quit)
        self.quit_button.pack(pady=10)

        self.root.mainloop()

    def player_chose_rock(self):
        self.play_game(0)

    def player_chose_paper(self):
        self.play_game(2)

    def player_chose_scissors(self):
        self.play_game(1)

    def get_computer_move(self):
        return random.choice(list(self.move_map.keys()))

    def get_winner(self, player_move, computer_move):
        if player_move == computer_move:
            return "It's a tie!"
        elif (player_move == 0 and computer_move == 1) or \
             (player_move == 1 and computer_move == 2) or \
             (player_move == 2 and computer_move == 0):
            return "You win!"
        else:
            return "You lose!"

    def play_game(self, player_move):
        self.game_counter += 1
        computer_move = self.get_computer_move()
        winner = self.get_winner(player_move, computer_move)

        # Record the game result in history
        game_result = {
            "Game #": self.game_counter,
            "Player Move": self.move_map[player_move],
            "Computer Move": self.move_map[computer_move],
            "Result": winner
        }
        self.history.append(game_result)

        # Update the history text widget
        self.history_text.insert(tk.END, f"Game #{self.game_counter}: Player chose {self.move_map[player_move]}, "
                                         f"Computer chose {self.move_map[computer_move]}. {winner}\n")
        self.history_text.see(tk.END)  # Auto-scroll to the end

        # Display a message box with the result
        messagebox.showinfo("Result", f"Player chose {self.move_map[player_move]}\n"
                                      f"Computer chose {self.move_map[computer_move]}\n\n"
                                      f"{winner}")

# Start the game
game = RockPaperScissorsGame()
