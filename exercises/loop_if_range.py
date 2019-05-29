
l = [] # void list

for x in range(10, 30):
    if x % 2 == 0 and x < 25:
        l.append(x)
    elif x >= 25:
        break

print(l)