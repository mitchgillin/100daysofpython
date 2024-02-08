# Sum heights without using sum() or len()
heights = [100, 134, 180, 95, 155, 190]

sum_heights = 0
total_heights = 0

for height in heights:
    sum_heights += height
    total_heights+=1 

avg_heights = sum_heights/total_heights

print(round(avg_heights, 2))
