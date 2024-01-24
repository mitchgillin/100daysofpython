print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
lor = input("You are at a cross road. Where do you want to go? (left/right)")

if lor == "right":
  print("Game Over :(")
else:
  lor = input("You come to a lake: Swim or wait for a boat?")
  if(lor == "swim"):
    print("Game Over :(")
  else:
    lor = input("You come to a series of doors: red, blue, yellow")
    if(lor == "yellow"):
      print("You win!")
    else:
      print("You died :(")
