print("Thank you for choosing Python Pizza Deliveries")

size= input("What size pizza do you want? (S/M/L)")
add_pepperoni = bool(input("Do you want Pepperoni? (True/False)"))
extra_cheese = bool(input("Do you want extra cheese? (True/False)"))
price = 0

if size == "S":
  price += 15
  if add_pepperoni:
    price+=2
elif size == "M":
  price += 20
  if add_pepperoni:
    price+=3
elif size =="L":
  price += 25
  if add_pepperoni:
    price+=3
if extra_cheese:
  price+=1

print(f"Your final bill is ${price}")
