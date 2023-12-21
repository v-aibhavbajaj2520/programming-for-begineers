import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


ran_password= []
for char in range (0, nr_letters):
  ran_password+= random.choice(letters)

for char in range(0,nr_numbers):
  ran_password+= random.choice(numbers)


for char in range(0,nr_symbols):
  ran_password+= random.choice(symbols)


# Shuffling a list
random.shuffle(ran_password)


# Creating empty string
actpass= ""
for char in ran_password:
  actpass+= char
print(f"Your {nr_letters+nr_symbols+nr_numbers} digit Password is {actpass}")

##########               OR                ##########

# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
# password1= str(password)
# lst=[]
# for letter in password1:
#  lst.append(letter)

# r= ""
# for ran in lst:
#   ran= random.randint(0,len(lst)-1)
#   q= password1[ran]
#   r += q
# print(r)


'''After generating password, asking user if he/she want to store it in a text file or not.
If yes, then asking for some details
including where it is being used and with which username'''

save= input("Do you want to save this password in a text file? (y/n) ")
if save=="y":
  app= input("Where it is being used? ")
  username= input("With which username? ")

  with open ("password.txt","a") as f:
    f.write(f"Your Password for {app} of username {username} is {actpass} \n")
    print("Password saved in password.txt.")
else:
  print("Password not saved.")