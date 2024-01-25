import random
# My choice will be [0-2], [rock, paper, scissors]
options = ["rock", "paper", "scissors"]
my_choice = int(input("0:rock, 1: paper: 2: scissors"))
comp_choice = random.randint(0,2) 
print(f"You chose {options[my_choice]}: your opponent chose {options[comp_choice]}")

if comp_choice == my_choice:
  print("It is a Tie!")
elif options[my_choice] == "rock":
  if options[comp_choice] == "paper":
    print("You lose")
  else:
    print("You win!")
elif options[my_choice] == "paper":
  if options[comp_choice] == "scissors":
    print("You lose")
  else:
    print("You win")
else:
  if options[comp_choice] == "rock":
    print("You lose")
  else:
    print("You win")
