import random

def play_game(player_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        return "It's a tie!"
    elif (
        (player_choice == "rock" and computer_choice == "scissors") or
        (player_choice == "paper" and computer_choice == "rock") or
        (player_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

player_choice = input("Enter your choice (rock, paper, scissors): ")
print(play_game(player_choice))