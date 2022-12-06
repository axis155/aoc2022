#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

packets = [lines[0][i] for i in range(len(lines[0]))]

for i in range(len(packets)-3):
    tempList = packets[i:i+4]
    if not set([x for x in tempList if tempList.count(x) > 1]):
        print("Answer 1")
        print(i + 4)
        break

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

packets = [lines[0][i] for i in range(len(lines[0]))]

for i in range(len(packets)-13):
    tempList = packets[i:i+14]
    if not set([x for x in tempList if tempList.count(x) > 1]):
        print("Answer 2")
        print(i + 14)
        break
