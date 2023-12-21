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

while input("Do you want to play? (True or False) ").lower() == "true":
    print("Choose 0 for Rock, 1 for Paper, and 2 for Scissors")
    player_choice = int(input("What do you want to choose? "))

    choices = [rock, paper, scissors]
    player_choice_text = choices[player_choice]
    print(f"Player chooses: {player_choice_text}")

    comp_choice = random.randint(0, 2)
    comp_choice_text = choices[comp_choice]
    print(f"Computer chooses: {comp_choice_text}")

    if player_choice == comp_choice:
        print("Match Ties")
    elif (player_choice == 0 and comp_choice == 1) or (player_choice == 1 and comp_choice == 2) or (
            player_choice == 2 and comp_choice == 0):
        print("Computer wins")
    else:
        print("Player wins")