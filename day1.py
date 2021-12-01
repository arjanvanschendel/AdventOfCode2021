elements = []
with open("day1input.txt", "r") as input_file:
    for line in input_file:
        elements.append(int(line.strip()))

counter = 0

for i in range (0, len(elements) - 1) :
    if elements[i] < elements[i+1]:
        counter += 1

print("Task 1: " + str(counter))

counter = 0

for i in range (0, len(elements) - 3) :
    firstwindow = elements[i] + elements[i+1] + elements[i+2]
    secondwindow = elements[i+1] + elements[i+2] + elements[i+3]
    if firstwindow < secondwindow:
        counter += 1

print("Task 2: " + str(counter))