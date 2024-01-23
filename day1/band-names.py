print("Day 1 - String Manipulation")
print("String Concatenation is done with the " + "+" +" sign.")
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Ask a user for their name and print the number of letters in the name
name = input("What is your name?")

print(name + " is " + str(len(name)) +" chars long")

# Switch the two variable values
a = 29
b = 41

temp = a
a = b
b = temp

print(a,b)

# Band Name Generator

print("Welcome to the Band Name Generator")

city = input("What is the name of the city you grew up in?")
pet_name = input("What is the name of your pet?")

print("Your band name is " + city + " " + pet_name)
