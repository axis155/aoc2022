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

            #print(value, isVis)
        return(isVis)
    else:
        return(0)
        

visibleCount = 0
for i in range(len(treeRows)):
    for j in range(len(treeRows[i])):
        visibleCount += checkVis(treeRows[i][j], i, j, len(treeRows[i]), len(treeRows))

print("Answer 1")
print(visibleCount)
