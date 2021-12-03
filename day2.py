elements = []
with open("day2input.txt", "r") as input_file:
    for line in input_file:
        elements.append(line.strip())

x = 0
y = 0

for i in range (0, len(elements)):
    direction = elements[i].split()[0]
    amount = elements[i].split()[1]
    if(direction == "forward"):
        x += int(amount)
    if(direction == "down"):
        y += int(amount)
    if(direction == "up"):
        y -= int(amount)

print("Task 1: (" + str(x) + "," + str(y) + ") = " + str(x*y))

x:int = 0
y:int = 0
aim:int = 0

for i in range (0, len(elements)):
    direction = elements[i].split()[0]
    amount = elements[i].split()[1]
    if(direction == "forward"):
        x += int(amount)
        y += aim*int(amount)
    if(direction == "down"):
        aim += int(amount)
    if(direction == "up"):
        aim -= int(amount)

print("Task 1: (" + str(x) + "," + str(y) + ") = " + str(x*y))