import random

def get_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid input. Please enter again.")
        user_choice = input("Enter your choice (rock/paper/scissors): ")
    return user_choice

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (user_choice == "rock" and computer_choice == "scissors") or \
       (user_choice == "scissors" and computer_choice == "paper") or \
       (user_choice == "paper" and computer_choice == "rock"):
        return "User wins!"
    return "Computer wins!"

def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose {user_choice}, computer chose {computer_choice}.")
    print(determine_winner(user_choice, computer_choice))

play_game()