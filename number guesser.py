import random
print('''Welcome to number guesser game!
In this game you have to guess a number between 1 to 100.''')
print("You have 5 chances to guess the number")
num=random.randint(1,100)
chances=5
hint1= input("Do you want a hint? y or n: ")
if hint1=="y":
    print("Here is your hint: ")
    if num>50:
        print("The number is greater than 50")
    else:
        print("The number is less than 50")
    print("You have 4 chances left.")
    chances-=1


while chances>0:
    guess=int(input("Enter the number: "))
    if guess==num:
        print("Wow! You guessed the number correctly in ",5-chances+1,"chances.")
        break
    else:
        if guess>num:
                if guess-num>10:
                    print("Your guess is too high.")
                    chances-=1
                    print("You have",chances,"chances left.")
                
                else:
                    print("Your guess is little high.")
                    chances-=1
                    print("You have",chances,"chances left.")
        else:
            if guess+10>num:
                print("Your guess is bit low.")
                chances-=1
                print("You have",chances,"chances left.")
                
            else:
                print("Your guess is too low.")
                chances-=1
                print("You have",chances,"chances left.")

if chances==0:
    print("You lost the game.")
    print("The number was",num)
    print("Better luck next time.")
print("Thanks for playing the game.")