import random

def rock_paper_scissors_game():
    """
    Plays a Rock-Paper-Scissors game between the user and the computer.
    
    The user is prompted to enter 'rock', 'paper', or 'scissors'.
    The computer randomly chooses one of the three options.
    The winner is determined based on the standard rules of the game.
    The game continues until the user decides to quit by entering 'quit'.
    """
    options = ["rock", "paper", "scissors"]

    user_input = str(input("rock, paper, scissors or quit >>> ")).lower()

    while user_input.lower() != "quit":
        machine_choice = options[random.randint(0, 2)]
        print(f"machine: {machine_choice}, user: {user_input}")
        if user_input == machine_choice:
            print("DRAW")
        elif machine_choice == "rock":
            if user_input == "paper":
                print("USER WINS!")
            else:
                print("MACHINE WINS!")
        elif machine_choice == "paper":
            if user_input == "scissors":
                print("USER WINS!")
            else:
                print("MACHINE WINS")
        elif machine_choice == "scissors":
            if user_input == "rock":
                print("USER WINS")
            else:
                print("MACHINE WINS!")
        user_input = str(input("rock, paper, scissors or quit >>> ")).lower()


# Run the game
rock_paper_scissors_game()
