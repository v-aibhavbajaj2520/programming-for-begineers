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

#Write your code below this line 👇
import random as r 
play = input("DO YOU WANT TO PLAY (True or False?) ")
while True:
  print("Choose 0 for Rock, 1 for Paper and 2 for Scissors ")
  player_choice= int(input("What do you want to choose? "))
  if player_choice== 0:
    print("Player chooses: " + rock )
  if player_choice== 1:
      print("Player chooses: " + paper )
  if player_choice== 2:
        print("Player chooses: " + scissors )
    


    
  comp_choice= r.randint(0,2)
  if comp_choice== 0:
    print ("Computer chooses: " + rock)
  if comp_choice== 1:
    print("Computer chooses: " + paper)
  if comp_choice== 2:
    print("Computer chooses: " + scissors)
  if player_choice== comp_choice:
    print("Match Ties")
  if player_choice== 0 and comp_choice==1:
    print("Computer wins")
  if player_choice== 0 and comp_choice==2:
    print("Player wins")
  if player_choice== 1 and comp_choice== 0:
    print("Player wins")
  if player_choice== 1 and comp_choice== 2:
    print("Computer wins")
  if player_choice== 2 and comp_choice== 0:
    print("Computer wins")
  if player_choice== 2 and comp_choice== 1:
    print("Player wins")