
#create a dictionary of the alphabet

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
alphaDict = dict((j,i+1) for i,j in enumerate(alphabet))

########## part 1 ###############
sumPriorities = 0

with open("rucksack.txt", "r") as rucksack:
    for line in rucksack:
        line = line.rstrip('\n')
        sack, sack_size = len(line), len(line)//2
        sackList = [ line[i:i+sack_size] for i in range(0, sack, sack_size) ]
        same = set(sackList[0]) & set(sackList[1])
        priority = alphaDict[list(same)[0]]
        #print(priority)
        #print(list(same)[0])
        #print(sackList)
        sumPriorities += priority

print(str(sumPriorities) + " is the sum of the priorities for the misplaced items")

rucksack.close()

############part 2####################
sumPriorities = 0
lineNumber = 1
#empty set
threeSacks = []
with open("rucksack.txt", "r") as rucksack:
    for line in rucksack:
        line = line.rstrip('\n')
        threeSacks.append(line)
        if lineNumber % 3 == 0:
            badge = set(threeSacks[0]) & set(threeSacks[1]) & set(threeSacks[2])
            #print(badge)
            priority = alphaDict[list(badge)[0]]
            sumPriorities += priority
            threeSacks.clear()

        lineNumber += 1
print(str(sumPriorities) + " is the sum of the priorities for the badges")
rucksack.close()
