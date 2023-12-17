print("Welcome to the Roller Coaster ride")
height=int(input("What is your height in cm?\n"))
bill= 0
if height >= 120:
  age=int(input("Enter your age\n"))
  if age<12:
    bill= 10 
    print("Child tickets is: ",bill)
  elif age<=18 and age>=12:
    bill= 15
    print("Youth tickets : ",bill)
  elif age>=45 and age<=55:
    bill= 0
    print("Aged tickets are free")
  else:
    bill= 20
    print("Adult tickets are $20")

# Asking person if they wanna include photo priced at $5
  photo= input("Do you want photo taken?\n Y or N ")
  if photo== 'Y':
    bill+= 5

  print(f"Your final bill is {bill}")
else:
  print("Sorry, you have to grow taller before you ride.")
