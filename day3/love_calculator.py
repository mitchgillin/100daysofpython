print("The Love Calculator is calculating your score...")
name1 = input("What is your name?")
name2 = input("What is their name?")
concat_name = name1.lower() +name2.lower()
### Calculate Love Score based on number of times [T R U E ] and [L O V E]
### appear in their names and concat TRUE with Love to get score

t = concat_name.count("t")
r = concat_name.count("r")
u = concat_name.count("u")

l = concat_name.count("l")
o = concat_name.count("o")
v = concat_name.count("v")
e = concat_name.count("e")

t_score = str(t+r+u+e)
l_score = str(l+o+v+e)

total_score = int(t_score + l_score)

if total_score >=90 or total_score <= 10:
  print(f"Your score is {total_score}: You go together well!")
elif total_score >=40 and total_score <= 50:
  print(f"Your score is {total_score}: You are alright together")
else:
  print(f"Your score is {total_score}")




