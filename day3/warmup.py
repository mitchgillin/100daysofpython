### Flow Control

print("Welcome to the Rollercoaster!")
height = int(input("What is your height in cm?"))
age = int(input("What is your age?"))
picture = bool(input("Do you want a photo? (True/False)") == "True")
ticket = 0;
if height >= 120:
  print("You can ride the rollercoaster!")
  if picture:
    ticket +=3
  if age >= 18 and age < 45 and age > 55:
    ticket +=12
    print(f"Your ticket price is ${ticket}")
  elif age >=45 and age <= 55:
    print(f"Your ticket price is ${ticket}")
  elif age >=12 and age < 18:
    ticket += 7
    print(f"Your ticket price is ${ticket}")
  else: 
    ticket += 5
    print(f"Your ticket price is ${ticket}")
else:
  print("Sorry, you have to grow taller to ride")


### Even or Odd?

print("Welcome to Even or Odd!")
num = int(input("Enter an integer"))

if num % 2 == 0:
  print("This is an even number")
else:
  print("This is an odd number")
