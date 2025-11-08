from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3 (computer)
number = randint(1,3)

# Turn that random number into the computer's RPS move
if number == 1:
    computer = "rock"
elif number == 2:
    computer = "paper"
elif number == 3:
    computer = "scissors"

# Ask a user to enter their move
player = input("Enter your move (“rock”, “paper”, or “scissors”): ").lower()

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
print("Your move: ")
if player == "rock":
    print(rock)
elif player == "paper":
    print(paper)
elif player == "scissors":
    print(scissors)

# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move
print("Computer's move: ")
if computer == "rock":
    print(rock)
elif computer == "paper":
    print(paper)
elif computer == "scissors":
    print(scissors)

# Figure out who wins and print the result!
if player == computer:
    print("It's a tie!")
elif player == "rock" and computer == "scissors":
    print("Player wins!")
elif player == "paper" and computer == "rock":
    print("Player wins!")
elif player == "scissors" and computer == "paper":
     print("Player wins!")
else:
    print("Computer wins!")