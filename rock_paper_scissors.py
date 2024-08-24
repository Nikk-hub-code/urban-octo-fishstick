import random
name = input("Enter your name= ").upper()
print(f"Hey!!{name}.")
print(f"""Winning rules of the game ROCK PAPER SCISSORS are :\n
       "Rock vs Paper -> Paper wins" \n
       "Rock vs Scissors -> Rock wins" \n
       "Paper vs Scissors -> Scissor wins" \n""")
while True:
       user_input = int(input("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n"))
       while user_input > 3 or user_input < 1:
              user_input = int(input("Please enter the valid choice= "))
       if user_input == 1:
              user_choice = 'Rock'
       elif user_input == 2:
              user_choice = 'Paper'
       else:
              user_choice = 'Scissors'
       print(f"{name} choice is {user_choice}")
       print(f"Now it's computer turns to choose")
       computer_choice = random.randint(1, 3)
       if computer_choice == 1:
              computer = 'Rock'
       elif computer_choice == 2:
              computer = 'Paper'
       else:
              computer = 'Scissors'
       print(f"Computer choice is {computer}")
       if user_input == computer_choice:
              print("Match draw.")
       elif user_input == 1 and computer_choice == 2:
              print("Computer Wins!")
       elif user_input == 1 and computer_choice == 3:
              print(f"{name} Wins!")
       elif user_input == 2 and computer_choice == 1:
              print(f"{name} Wins!")
       elif user_input == 2 and computer_choice == 3:
              print(f"Computer Wins!")
       elif user_input == 3 and computer_choice == 1:
              print("Computer Wins!")
       elif user_input == 3 and computer_choice == 2:
              print(f"{name} Wins!")
       print("Do you want to play again? (Y/N)")
       repeat = input().lower()
       if repeat == 'n':
              break
print("THANKS FOR PLAYING")