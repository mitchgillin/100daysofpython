print("Welcome to the Tip Calculator");

total = float(input("What was the total bill?"))
split = int(input("How many people are splitting the bill?"))
percent = float(input("What percent tip would you like to give?"))

pp_split = total/split
percent = percent/100
pp_percent = pp_split*percent

pp_total = round(pp_split + pp_percent, 2)

print("Each person should pay $"+ str(pp_total))
