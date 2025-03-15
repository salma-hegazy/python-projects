import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

while True:
    user_choice = int(input("What do you choose? Type 1 for Rock, 2 for Paper, and 3 for Scissors\n")) - 1
    computer_choice = random.randint(0, 2)

    if user_choice < 0 or user_choice > 2:
        print("Invalid choice! Please select a valid option (1-3).")
        continue

    print(f"Your choice is {choice[user_choice]}")
    print(f"The computer's choice is {choice[computer_choice]}")

    if user_choice == computer_choice:
        print("It's a draw!")
    elif user_choice == 0:  # Rock
        if computer_choice == 1:
            print("You lost!")
        else:
            print("You won!")
    elif user_choice == 1:  # Paper
        if computer_choice == 2:
            print("You lost!")
        else:
            print("You won!")
    elif user_choice == 2:  # Scissors
        if computer_choice == 0:
            print("You lost!")
        else:
            print("You won!")

    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != "yes":
        print("Thanks for playing! Goodbye!")
        break
