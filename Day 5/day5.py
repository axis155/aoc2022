import re

#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#Workout maximum height of stacks to limit the creation of lists later
maxHeight = 0
for i in range(len(lines)):
    if not lines[i][1].isnumeric():
        maxHeight += 1
    else:
        break

#Workout how many stacks there are
maxStacks = 0
for i in range(maxHeight):
    if len(lines[i]) > maxStacks:
        maxStacks = len(lines[i])

#Create stack lists
stack = [[] for i in range(maxStacks//4 + 1)]

#Populate stacks
for i in range(len(stack)):
    for j in range(maxHeight):
        if len(lines[j]) > (1 + (i * 4)):
            if lines[j][1 + (i * 4)].isalpha():
                stack[i].append(lines[j][1 + (i * 4)])
    stack[i].reverse()

#Movements
for i in range(maxHeight + 2, len(lines)):
    m = re.search('move (.+?) from', lines[i])
    moveStacks = m.group(1)
    f = re.search('from (.+?) to', lines[i])
    fromStack = f.group(1)
    toStack = re.sub(r'^.*?to ', '', lines[i])
    for j in range(int(moveStacks)):
        movedCrate = stack[int(fromStack)-1][-1]
        stack[int(fromStack)-1].pop()
        stack[int(toStack)-1].append(movedCrate)

print("Answer 1")
for i in range(len(stack)):
    print(stack[i][-1], end = " ")

print("")
import re

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

#Workout maximum height of stacks to limit the creation of lists later
maxHeight = 0
for i in range(len(lines)):
    if not lines[i][1].isnumeric():
        maxHeight += 1
    else:
        break

#Workout how many stacks there are
maxStacks = 0
for i in range(maxHeight):
    if len(lines[i]) > maxStacks:
        maxStacks = len(lines[i])

#Create stack lists
stack = [[] for i in range(maxStacks//4 + 1)]

#Populate stacks
for i in range(len(stack)):
    for j in range(maxHeight):
        if len(lines[j]) > (1 + (i * 4)):
            if lines[j][1 + (i * 4)].isalpha():
                stack[i].append(lines[j][1 + (i * 4)])
    stack[i].reverse()

#Movements
for i in range(maxHeight + 2, len(lines)):
    m = re.search('move (.+?) from', lines[i])
    moveStacks = m.group(1)
    f = re.search('from (.+?) to', lines[i])
    fromStack = f.group(1)
    toStack = re.sub(r'^.*?to ', '', lines[i])
    
    movedCrates = stack[int(fromStack)-1][-int(moveStacks):]
    del stack[int(fromStack)-1][-int(moveStacks):]
    stack[int(toStack)-1] = stack[int(toStack)-1] + movedCrates

print("Answer 2")
for i in range(len(stack)):
    print(stack[i][-1], end = " ")
    

    
