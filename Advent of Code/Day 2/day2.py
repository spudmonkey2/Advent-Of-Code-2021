input = open("directions.txt","r")
commands = input.readlines()
print(commands[1])
num = "forward 5"
hor = 0
depth = 0
aim = 0
for x in range(len(commands)):
    if commands[x].startswith('forward'):
        ListHor = commands[x].split(" ")
        hor += int(ListHor[1])
        math = aim * int(ListHor[1])
        depth += math
    if commands[x].startswith('up'):
        ListUp = commands[x].split(" ")
        #depth -= int(ListUp[1])
        aim -= int(ListUp[1])
    if commands[x].startswith('down'):
        ListDown = commands[x].split(" ")
        #depth += int(ListDown[1])
        aim += int(ListDown[1])
total = hor * depth
print(hor)
print(depth)
print(total)