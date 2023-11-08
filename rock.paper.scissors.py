import random
choices = ["rock", "paper", "scissors"]
while True:
    player_choices = input("Choose your choice (rock, paper, scissors) to play or press Enter to quit: ").lower()
    
    if not player_choices:
        break
    computer_choices = random.choice(choices)
    print(f"Computer chose {computer_choices}")
    if player_choices in choices:
        if player_choices == computer_choices:
            print("Match tie")
        elif (player_choices == 'rock' and computer_choices == 'scissors') or \
             (player_choices == 'scissors' and computer_choices == 'paper') or \
             (player_choices == 'paper' and computer_choices == 'rock'):
            print("You win")
        else:
            print("Computer wins")
    else:
        print("Invalid choice. Please choose Rock, Paper, or Scissors.")
