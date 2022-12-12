import math

#Part 1
lines = [line.rstrip() for line in open("data.txt")]
    
headMoves = [["S",0,0]]
tailMoves = [[0,0]]

def moveTail(prevMove, currMove):
    #Check to see if start of the movement
    if (len(headMoves) >= 2):
        #Check if x and y of tailMoves are within +/- 1 of headMoves
        tempMove = currMove[1:]
        tempCheck = list(zip(tempMove, tailMoves[-1]))
        if (math.dist((tempCheck[0][0],),(tempCheck[0][1],)) > 1) or (math.dist((tempCheck[1][0],),(tempCheck[1][1],)) > 1):
            #Moving the tail
            if (currMove[0][:1] == "U"):
                tailMoves.append([(int(currMove[1])), (int(currMove[2]) + 1)])
            elif (currMove[0][:1] == "D"):
                tailMoves.append([(int(currMove[1])), (int(currMove[2]) - 1)])
            elif (currMove[0][:1] == "R"):
                tailMoves.append([(int(currMove[1])) - 1, (int(currMove[2]))])
            elif (currMove[0][:1] == "L"):
                tailMoves.append([(int(currMove[1])) + 1, (int(currMove[2]))])

#Head Moves
for i in range(len(lines)):
    #Right
    if lines[i][:1] == "R":
        for j in range(int(lines[i].split()[1])):
            headMoves.append([lines[i], int(headMoves[-1][1]) + 1, int(headMoves[-1][2])])
            moveTail(headMoves[-2], headMoves[-1])
    #Up
    elif lines[i][:1] == "U":
        for j in range(int(lines[i].split()[1])):
            headMoves.append([lines[i], int(headMoves[-1][1]), int(headMoves[-1][2]) - 1])
            moveTail(headMoves[-2], headMoves[-1])
    #Left
    elif lines[i][:1] == "L":
        for j in range(int(lines[i].split()[1])):
            headMoves.append([lines[i], int(headMoves[-1][1]) - 1, headMoves[-1][2]])
            moveTail(headMoves[-2], headMoves[-1])
    #Down
    elif lines[i][:1] == "D":
        for j in range(int(lines[i].split()[1])):
            headMoves.append([lines[i], int(headMoves[-1][1]), int(headMoves[-1][2]) + 1])
            moveTail(headMoves[-2], headMoves[-1])

print("Answer 1")

#Removing duplicates
tailMovesDist = []
for i in tailMoves:
    if i in tailMovesDist:
        continue
    else:
        tailMovesDist.append(i)

print(len(tailMovesDist))
