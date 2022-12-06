stack1 = ['V','C','D','R','Z','G','B','W']
stack2 = ['G','W','F','C','B','S','T','V']
stack3 = ['C','B','S','N','W']
stack4 = ['Q','G','M','N','J','V','C','P']
stack5 = ['T','S','L','F','D','H','B']
stack6 = ['J','V','T','W','M','N']
stack7 = ['P','F','L','C','S','T','G']
stack8 = ['B','D','Z']
stack9 = ['M','N','Z','W']


with open("boxMoves.txt", "r") as moves:
    for line in moves:
        numberOfMoves = 0
        delimintedMoves = line.rsplit()
        #number of boxes is delimintedMoves[1]
        #column/list to move FROM is delimintedMoves[3]
        #column/list to move TO is delimintedMoves[5]
        fromStack = "stack" + str(delimintedMoves[3])
        toStack = "stack" + str(delimintedMoves[5])
        fromStackVar = vars()[fromStack]
        toStackVar = vars()[toStack]
        depth = len(fromStackVar) - int(delimintedMoves[1])

        for numberOfBoxes in range(int(delimintedMoves[1])):
            crate = fromStackVar.pop(depth)
            toStackVar.append(crate)



            
            numberOfMoves += 1


print(stack1[len(stack1)-1],stack2[len(stack2)-1],stack3[len(stack3)-1],stack4[len(stack4)-1],stack5[len(stack5)-1],stack6[len(stack6)-1],stack7[len(stack7)-1],stack8[len(stack8)-1],stack9[len(stack9)-1],sep='' )
        
