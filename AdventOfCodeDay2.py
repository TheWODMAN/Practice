scoreRock = 1
scorePaper = 2
scoreScissors = 3
scoreWin = 6
scoreTie = 3

myScore = 0
opponentScore = 0


with open('encryptedStrategyGuide.txt', 'r') as f:
    for line in f:
        gesture = line.rsplit()
        opponentGesture = gesture[0]
        myGesture = gesture[1]

        #make the elf's stuff the same as mine.  I don't want to do compares A == X when they are the same gesture
        if opponentGesture == 'A':
            opponentGestureTranposed = 'rock'
        elif opponentGesture == 'B':
            opponentGestureTranposed = 'paper'
        elif opponentGesture == 'C':
            opponentGestureTranposed = 'scissors'
        
        

        #make the my stuff readable and the same as the elf
        if myGesture == 'X':
            myGestureTransposed = 'rock'
        elif myGesture == 'Y':
            myGestureTransposed = 'paper'
        elif myGesture == 'Z':
            myGestureTransposed = 'scissors'
      
            
        
#can't use a tie condition since the score can SOMEHOW be different just by selecting a different gesture
        #I'm going rock
        if myGestureTransposed == "rock":
            myScore += scoreRock

                #win
            if opponentGestureTranposed == "scissors":
                opponentScore += scoreScissors
                myScore += scoreWin

                #loss
            elif opponentGestureTranposed == "paper":
                opponentScore += scorePaper
                opponentScore += scoreWin

                #same same, tie
            elif opponentGestureTranposed == "rock":
                opponentScore += scoreRock
                myScore += scoreTie
                opponentScore += scoreTie
        #I'm going paper
        elif myGestureTransposed == "paper":
            myScore += scorePaper

                #win
            if opponentGestureTranposed == "rock":
                opponentScore += scoreRock
                myScore += scoreWin

                #loss
            elif opponentGestureTranposed == "scissors":
                opponentScore += scoreScissors
                opponentScore += scoreWin

                #same same tie
            elif opponentGestureTranposed == "paper":
                opponentScore += scorePaper
                myScore += scoreTie
                opponentScore += scoreTie
        #I'm going scissors
        elif myGestureTransposed == "scissors":
            myScore += scoreScissors
                #win
            if opponentGestureTranposed == "paper":
                opponentScore += scorePaper
                myScore += scoreWin

                #loss
            elif opponentGestureTranposed == "rock":
                opponentScore += scoreRock
                opponentScore += scoreWin

                #same same tie
            elif opponentGestureTranposed == "scissors":
                opponentScore += scoreScissors
                myScore += scoreTie
                opponentScore += scoreTie


   
print("My score for part 1 would be " + str(myScore))
print("Opponent's score for part 1 would be " + str(opponentScore))
        
        
        

        
f.close

myScore = 0
opponentScore = 0

with open('encryptedStrategyGuide.txt', 'r') as f:
    for line in f:
        gameCondition = line.rsplit()
        opponentGesture = gameCondition[0]
        result = gameCondition[1]

        #make the elf's stuff the same as mine.  I don't want to do compares A == X when they are the same gesture
        if opponentGesture == 'A':
            opponentGestureTranposed = 'rock'
        elif opponentGesture == 'B':
            opponentGestureTranposed = 'paper'
        elif opponentGesture == 'C':
            opponentGestureTranposed = 'scissors'
        
        

        #make the my stuff readable and the same as the elf
        if result == 'X':
            resultTransposed = 'loss'
        elif result == 'Y':
            resultTransposed = 'tie'
        elif result == 'Z':
            resultTransposed = 'win'

        #print(opponentGesture, opponentGestureTranposed, result, resultTransposed)
      
    
        
#can't use a tie condition since the score can SOMEHOW be different just by selecting a different gesture
        #have to queue of opponents gesture instead
        #opponent going rock
        if opponentGestureTranposed == "rock":
            opponentScore += scoreRock

                #win
            if resultTransposed == "win":
                myScore += scorePaper
                myScore += scoreWin
                

                #loss
            elif resultTransposed == "loss":
                myScore += scoreScissors
                opponentScore += scoreWin
               

                #same same, tie
            elif resultTransposed == "tie":
                myScore += scoreRock
                myScore += scoreTie
                opponentScore += scoreTie
                

        #opponent going paper
        elif opponentGestureTranposed == "paper":
            opponentScore += scorePaper

                #win
            if resultTransposed == "win":
                myScore += scoreScissors
                myScore += scoreWin
                

                #loss
            elif resultTransposed == "loss":
                myScore += scoreRock
                opponentScore += scoreWin
               
                

                #same same tie
            elif resultTransposed == "tie":
                myScore += scorePaper
                myScore += scoreTie
                opponentScore += scoreTie
                

        #opponent going scissors
        elif opponentGestureTranposed == "scissors":
            opponentScore += scoreScissors
                #win
            if resultTransposed == "win":
                myScore += scoreRock
                myScore += scoreWin
               

                #loss
            elif resultTransposed == "loss":
                myScore += scorePaper
                opponentScore += scoreWin
                

                #same same tie
            elif resultTransposed == "tie":
                myScore += scoreScissors
                myScore += scoreTie
                opponentScore += scoreTie
              

print("My score for part 2 would be " + str(myScore))
print("Opponent's score for part 2 would be " + str(opponentScore))
        

f.close