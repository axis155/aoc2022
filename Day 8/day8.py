#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#Set up grid
treeRows = [[] for i in range(len(lines))]
for i in range(len(treeRows)):
    treeRows[i] = []
    for j in range(len(lines[i])):
        treeRows[i].append(lines[i][j])

def checkVis(value, rowNum, colNum, maxRow, maxCol):
    #Count corners first - TL, BL, TR, BR
    if (rowNum == 0) and (colNum == 0):
        return(1)
    elif (colNum == 0) and (rowNum == maxRow - 1):
        return(1)
    elif (rowNum == 0) and (colNum == maxCol - 1):
        return(1)
    elif (rowNum == maxRow - 1) and (colNum == maxCol - 1):
        return(1)
    #Count first column
    elif colNum == 0:
        return(1)
    #Count last column
    elif (colNum == maxCol - 1):
        return(1)
    #Count first row
    elif rowNum == 0:
        return(1)
    #Count last row
    elif rowNum == maxRow - 1:
        return(1)
    #Check anything not on edge
    elif (colNum > 0) and (colNum < maxCol - 1) and (rowNum > 0) and (rowNum < maxRow - 1):
        #Check left
        j = 0
        while (j < colNum):
            isVis = 1
            if (int(treeRows[rowNum][j]) >= int(value)):
                isVis = 0
                break
            j += 1
        #Check right
        if (isVis == 0):
            j = maxCol - 1
            while (j > colNum):
                isVis = 1
                if (int(treeRows[rowNum][j]) >= int(value)):
                    isVis = 0
                    break
                j -= 1
        #Check down
        if (isVis == 0):
            j = maxRow - 1
            while (j > rowNum):
                isVis = 1
                if (int(treeRows[j][colNum]) >= int(value)):
                    isVis = 0
                    break
                j -= 1
        #Check up
        if (isVis == 0):
            j = 0
            while (j < rowNum):
                isVis = 1
                if (int(treeRows[j][colNum]) >= int(value)):
                    isVis = 0
                    break                
                j += 1
        return(isVis)
    else:
        return(0)
        
visibleCount = 0
for i in range(len(treeRows)):
    for j in range(len(treeRows[i])):
        visibleCount += checkVis(treeRows[i][j], i, j, len(treeRows[i]), len(treeRows))

print("Answer 1")
print(visibleCount)

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#Set up grid
treeRows = [[] for i in range(len(lines))]
for i in range(len(treeRows)):
    treeRows[i] = []
    for j in range(len(lines[i])):
        treeRows[i].append(lines[i][j])

def calcScore(value, rowNum, colNum, maxRow, maxCol):
    #Ignore corners first - TL, BL, TR, BR
    if (rowNum == 0) and (colNum == 0):
        return(0)
    elif (colNum == 0) and (rowNum == maxRow - 1):
        return(0)
    elif (rowNum == 0) and (colNum == maxCol - 1):
        return(0)
    elif (rowNum == maxRow - 1) and (colNum == maxCol - 1):
        return(0)
    #Ignore first column
    elif colNum == 0:
        return(0)
    #Ignore last column
    elif (colNum == maxCol - 1):
        return(0)
    #Ignore first row
    elif rowNum == 0:
        return(0)
    #Ignore last row
    elif rowNum == maxRow - 1:
        return(0)
    #Check anything not on edge
    elif (colNum > 0) and (colNum < maxCol - 1) and (rowNum > 0) and (rowNum < maxRow - 1):
        totalCount = 0
        #Look up
        if (rowNum == 1):
            upCount = 1
        else:
            upCount = 1
            j = rowNum - 1
            while (j > 0):
                if (int(treeRows[j][colNum]) >= int(value)):
                    break                
                j -= 1
                upCount += 1
        #Look left
        if (colNum == 1):
            leftCount = 1
        else:
            leftCount = 1
            j = colNum - 1
            while (j > 0):
                if (int(treeRows[rowNum][j]) >= int(value)):
                    break
                j -= 1
                leftCount += 1
        #Look down
        if (rowNum == maxRow - 2):
            downCount = 1
        else:
            downCount = 1
            j = rowNum + 1
            while (j <= maxRow - 1):
                if (int(treeRows[j][colNum]) >= int(value)):
                    break
                j += 1
                downCount += 1
        #Look right
        if (colNum == maxCol - 2):
            rightCount = 1
        else:
            rightCount = 1
            j = colNum + 1
            while (j < maxCol - 1):
                if (int(treeRows[rowNum][j]) >= int(value)):
                    break
                j += 1
                rightCount += 1
        totalCount = leftCount * rightCount * downCount * upCount
        return(totalCount)
    else:
        return(0)
        
scenicScore = 0
for i in range(len(treeRows)):
    for j in range(len(treeRows[i])):
        tempScore = calcScore(treeRows[i][j], i, j, len(treeRows[i]), len(treeRows))
        if tempScore > scenicScore:
            scenicScore = tempScore
        
print("Answer 2")
print(scenicScore)
