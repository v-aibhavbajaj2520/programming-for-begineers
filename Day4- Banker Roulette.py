import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 👆 splits number of stings by given character and forms a list

# Generating random digit 
a= len(names)
b= random.randint(0,a-1)
# Using random digit to find out name 
payer =names[b]
#
print(payer+ " is going to buy the meal today!")

# ------ OPTIONAL CODE -------
# payer= random.choice(names)
# print(payer+ " is going to buy the meal today!")
