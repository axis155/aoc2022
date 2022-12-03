#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

calCount = []
tempCount = 0

for i in range(len(lines)):
    if lines[i]:
        tempCount += int(lines[i])
    else:
        calCount.append(tempCount)
        tempCount = 0

calCount.append(tempCount)

calCount.sort(reverse=True)

print("Answer 1")
print(calCount[0])


#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

calCount = []
tempCount = 0

for i in range(len(lines)):
    if lines[i]:
        tempCount += int(lines[i])
    else:
        calCount.append(tempCount)
        tempCount = 0
        
calCount.append(tempCount)

calCount.sort(reverse=True)

print("Answer 2")
print(calCount[0] + calCount[1] + calCount[2])


