import random

states_of_america =["Delaware", "Pennsylvania", "New Jersey"]

# Python is 0-indexed
print(states_of_america[0])

# Python has negative indices
print(states_of_america[-1])

# Create a bill pay roulette 

names = ["Mitch", "Mark", "Michael","Joseph", "Ryan"]

payer = names[random.randint(0,len(names)-1)]

print(payer)

line1 = ["O", "O", "O"]
line2 = ["O", "O", "O"]
line3 = ["O", "O", "O"]

map = [line1,line2,line3]

treasure_location = input("Enter location [A-C][0-2]")

my_map = {"A": 0, "B":1,"C":2}

treasure_x = int(my_map[treasure_location[0]])
treasure_y = int(treasure_location[1])

map[treasure_x][treasure_y] = "X"

print(f"{map[0]}\n{map[1]}\n{map[2]}")
