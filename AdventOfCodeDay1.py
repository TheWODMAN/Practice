elves = []
calsCarrying = 0
with open("calorie.txt", "r") as calories:
    for line in calories:
        if line.strip():
            calsCarrying += int(line)
        else:
            elves.append(calsCarrying)
            calsCarrying = 0
elves.sort()
print(elves)




