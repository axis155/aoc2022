#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

score = 0
for i in range(len(lines)):
    tempLine = lines[i].split()
    if tempLine[0] == "A":
        if tempLine[1] == "X":
            score += 4
        elif tempLine[1] == "Y":
            score += 8
        elif tempLine[1] == "Z":
            score += 3
    elif tempLine[0] == "B":
        if tempLine[1] == "X":
            score += 1
        elif tempLine[1] == "Y":
            score += 5
        elif tempLine[1] == "Z":
            score += 9
    elif tempLine[0] == "C":
        if tempLine[1] == "X":
            score += 7
        elif tempLine[1] == "Y":
            score += 2
        elif tempLine[1] == "Z":
            score += 6

print("Answer 1")    
print(score)

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

score = 0
for i in range(len(lines)):
    tempLine = lines[i].split()
    if tempLine[0] == "A":
        if tempLine[1] == "X":
            score += 3 + 0
        elif tempLine[1] == "Y":
            score += 1 + 3
        elif tempLine[1] == "Z":
            score += 2 + 6
    elif tempLine[0] == "B":
        if tempLine[1] == "X":
            score += 1 + 0
        elif tempLine[1] == "Y":
            score += 2 + 3
        elif tempLine[1] == "Z":
            score += 3 + 6
    elif tempLine[0] == "C":
        if tempLine[1] == "X":
            score += 2 + 0
        elif tempLine[1] == "Y":
            score += 3 + 3
        elif tempLine[1] == "Z":
            score += 1 + 6

print("Answer 2")    
print(score)

