import sys
sys.path.append('../util')
from util.binaryCounter import BinaryCounter

elements = []
with open("./input/day3input.txt", "r") as input_file:
    for line in input_file:
        elements.append(line.strip())

itemlength = len(elements[0])
counters = [BinaryCounter() for i in range (0, itemlength)]

for i in range (0, len(elements)):
    for j in range (0, itemlength):
        if(elements[i][j] == str(0)):
            counters[j].zerocount += 1
        if(elements[i][j] == str(1)):
            counters[j].onecount += 1

gammaRate = ""
epsilonRate = ""

for i in range (0, itemlength):
    gammaRate = gammaRate + str(counters[i].most())
    epsilonRate = epsilonRate + str(counters[i].least())

gammaRateInt = int(gammaRate, 2)
epsilonRateInt = int(epsilonRate, 2)

print("Task 1: " + str(gammaRateInt*epsilonRateInt))

def most_common_at_index(input:list, index:int):
    countZero = 0
    countOne = 0
    for i in range(0,len(input)):
        if(int(input[i][index]) == 0):
            countZero += 1
        if(int(input[i][index]) == 1):
            countOne += 1

    if(countZero > countOne):
        return 0
    return 1

def least_common_at_index(input:list, index: int):
    if(most_common_at_index(input, index) == 0):
        return 1
    return 0

def all_with_most_common_at_index(input:list, index: int):
    filterNumber = most_common_at_index(input, index)
    toReturn = []
    for i in range(0, len(input)):
        if(int(input[i][index]) == int(filterNumber)):
            toReturn.append(input[i])
    return toReturn

def all_with_least_common_at_index(input: list, index:int):    
    filterNumber = least_common_at_index(input, index)
    toReturn = []
    for i in range(0, len(input)):
        if(int(input[i][index]) == int(filterNumber)):
            toReturn.append(input[i])
    return toReturn

oxygenGeneratorRating = elements
co2ScrubberRating = elements

for i in range(0, itemlength):
    if(len(oxygenGeneratorRating) > 1):
        oxygenGeneratorRating = all_with_most_common_at_index(oxygenGeneratorRating, i)
        
    if(len(co2ScrubberRating) > 1):
        co2ScrubberRating = all_with_least_common_at_index(co2ScrubberRating, i)


print(oxygenGeneratorRating[0] + ", " + co2ScrubberRating[0])
print("Task 2: " + str(int(oxygenGeneratorRating[0], 2) * int(co2ScrubberRating[0], 2)))