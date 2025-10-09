# goal 2 #

Numbers = [10, 20, 30, 40, 50]

print(Numbers[2])
print(Numbers[3:])
total = 0
for i in range(len(Numbers)):
    total += Numbers[i]
    print("Total:", total)

for i in range(len(Numbers)): 
    print(f"Position {i + 1}: {Numbers[i]}")