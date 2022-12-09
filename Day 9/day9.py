#Part 1
with open('testdata.txt') as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]
