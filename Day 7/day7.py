#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

folders = {}
currPath = []

for i in range(len(lines)):
    if (lines[i][:5] == "$ cd ") and (lines[i + 1] == "$ ls"):
        currDir = lines[i][5:]
        currPath.append(currDir)
        currPathStr = ' '.join(str(e) for e in currPath)
        if currDir not in folders:
            folders.update({currPathStr: 0})
    elif (lines[i] == "$ cd .."):
        currPath.pop()
    elif (lines[i].split(" ")[0].isnumeric()):
        for j in folders:
             if (j in currPathStr):
                folders[j] += int(lines[i].split(" ")[0])

currSum = 0
for x in folders:
    if folders[x] <= 100000:
        currSum += folders[x]

print("Answer 1")
print(currSum)

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

folders = {}
currPath = []

for i in range(len(lines)):
    if (lines[i][:5] == "$ cd ") and (lines[i + 1] == "$ ls"):
        currDir = lines[i][5:]
        currPath.append(currDir)
        currPathStr = ' '.join(str(e) for e in currPath)
        if currDir not in folders:
            folders.update({currPathStr: 0})
    elif (lines[i] == "$ cd .."):
        currPath.pop()
    elif (lines[i].split(" ")[0].isnumeric()):
        for j in folders:
             if (j in currPathStr):
                folders[j] += int(lines[i].split(" ")[0])

for j in folders:
    if (j == "/"):
        totalSize = folders[j]

folders = {k: v for k, v in sorted(folders.items(), key = lambda x: x[1])}

deleteSize = 0
for j in folders:
    if ((70000000 - totalSize + folders[j]) > 30000000):
        deleteSize = folders[j]
        break

print("Answer 2")
print(deleteSize)
