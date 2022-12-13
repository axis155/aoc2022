#Part 1
lines = [line.rstrip() for line in open("data.txt")]

cycleCount = 0
x = 1
signalStrength = 0

def checkCycle(x, cycleCount):
    if (cycleCount in [20, 60, 100, 140, 180, 220]):
        global signalStrength
        signalStrength += cycleCount * x

for i in range(len(lines)):
    if (lines[i] == "noop"):   
        cycleCount += 1
        checkCycle(x, cycleCount)
    else:
        for j in range(2):
            cycleCount += 1
            checkCycle(x, cycleCount)
            if j == 1:
                x += int(lines[i].split()[1])
            

print("Answer 1")
print(signalStrength)
