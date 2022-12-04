#Part 1
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

count = 0

for i in range(len(lines)):
    temp = lines[i].split(',')
    elf1 = temp[0].split('-')
    elf2 = temp[1].split('-')

    if int(elf1[0]) >= int(elf2[0]):
        if int(elf1[1]) <= int(elf2[1]):
            count += 1
    if int(elf2[0]) >= int(elf1[0]):
        if int(elf2[1]) <= int(elf1[1]):
            count += 1
    if int(elf1[0]) == int(elf2[0]):
        if int(elf1[1]) == int(elf2[1]):
            count -= 1

print("Answer 1")
print(count)

#Part 2
with open('data.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

count = 0

for i in range(len(lines)):
    temp = lines[i].split(',')
    elf1 = temp[0].split('-')
    elf2 = temp[1].split('-')
    
    if int(elf1[0]) >= int(elf2[0]) and int(elf1[0]) <= int(elf2[1]):
        count += 1
    elif int(elf2[0]) >= int(elf1[0]) and int(elf2[0]) <= int(elf1[1]):
        count += 1

print("Answer 2")
print(count)
