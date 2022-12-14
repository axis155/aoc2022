import re, math
#Part 1
lines = [line.rstrip() for line in open("data.txt")]

#Count number of monkeys to create lists
monkeyCount = 0
for i in range(len(lines)):
    if (lines[i][:6] == "Monkey"):
        monkeyCount += 1

#Create list for each monkey             
monkeyItems = [[] for i in range(monkeyCount)]

#Create list for operations, test and targets
monkeyDets = [[] for i in range(monkeyCount)]

#Populate monkey items and details lists with initial data
for i in range(len(lines)):
    if (lines[i][:6] == "Monkey"):
        monkeyNumber = int(lines[i][7:8])
        #Monkey Items
        itemsLines = lines[i+1][17:]
        items = itemsLines.split(", ")
        for item in items: monkeyItems[monkeyNumber].append(int(item))
        #Monkey details
        monkeyDets[monkeyNumber].append(re.sub(r'^.*?old ', '', lines[i + 2]))
        monkeyDets[monkeyNumber].append(int(re.sub(r'^.*?by ', '', lines[i + 3])))
        monkeyDets[monkeyNumber].append(int(lines[i + 4][-1]))
        monkeyDets[monkeyNumber].append(int(lines[i + 5][-1]))
            
#Create list of throw counts
throwCount = [[0] for i in range(len(monkeyItems))]

for turn in range(20):
    for monkey in range(monkeyCount):
        for item in range(len(monkeyItems[monkey])):
            throwCount[monkey][0] += 1
            initWorryLvl = str(monkeyItems[monkey][item])
            operation = initWorryLvl + monkeyDets[monkey][0]
            if ("old" in monkeyDets[monkey][0]):
                operation = operation.replace("old", initWorryLvl)
            opWorryLvl = eval(operation)
            boredWorryLvl = math.trunc(opWorryLvl/3)
            if (boredWorryLvl % int(monkeyDets[monkey][1]) == 0):
                monkeyItems[int(monkeyDets[monkey][2])].append(boredWorryLvl)
            else:
                monkeyItems[int(monkeyDets[monkey][3])].append(boredWorryLvl)
        monkeyItems[monkey] = []

print("Answer 1")
throwCount.sort()
print(throwCount[-1][0] * throwCount[-2][0])


#Part 2
lines = [line.rstrip() for line in open("testdata.txt")]

#Count number of monkeys to create lists
monkeyCount = 0
for i in range(len(lines)):
    if (lines[i][:6] == "Monkey"):
        monkeyCount += 1

#Create list for each monkey             
monkeyItems = [[] for i in range(monkeyCount)]

#Create list for operations, test and targets
monkeyDets = [[] for i in range(monkeyCount)]

#Populate monkey items and details lists with initial data
for i in range(len(lines)):
    if (lines[i][:6] == "Monkey"):
        monkeyNumber = int(lines[i][7:8])
        #Monkey Items
        itemsLines = lines[i+1][17:]
        items = itemsLines.split(", ")
        for item in items: monkeyItems[monkeyNumber].append(int(item))
        #Monkey details
        monkeyDets[monkeyNumber].append(re.sub(r'^.*?old ', '', lines[i + 2]))
        monkeyDets[monkeyNumber].append(int(re.sub(r'^.*?by ', '', lines[i + 3])))
        monkeyDets[monkeyNumber].append(int(lines[i + 4][-1]))
        monkeyDets[monkeyNumber].append(int(lines[i + 5][-1]))
            
#Create list of throw counts
throwCount = [[0] for i in range(len(monkeyItems))]

for turn in range(20):
    for monkey in range(monkeyCount):
        for item in range(len(monkeyItems[monkey])):
            throwCount[monkey][0] += 1
            initWorryLvl = str(monkeyItems[monkey][item])
            operation = initWorryLvl + monkeyDets[monkey][0]
            if ("old" in monkeyDets[monkey][0]):
                operation = operation.replace("old", initWorryLvl)
                opWorryLvl = eval(operation)
                opWorryLvl = opWorryLvl % int(monkeyDets[monkey][1])
            else:
                opWorryLvl = eval(operation)
            if (opWorryLvl % int(monkeyDets[monkey][1] == 0)):
                monkeyItems[int(monkeyDets[monkey][2])].append(modWorryLvl)
            else:
                monkeyItems[int(monkeyDets[monkey][3])].append(modWorryLvl)
        monkeyItems[monkey] = []

print("Answer 2")
throwCount.sort()
print(throwCount)
print(throwCount[-1][0] * throwCount[-2][0])
