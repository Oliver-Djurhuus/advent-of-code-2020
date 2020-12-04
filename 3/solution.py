import sys
import json

parameters = json.load(open("input.json", "r"))

def getTreeEncounters(right, down):
    repeats = int((len(parameters['input']) * right + 1) / len(parameters['input'][0])) + 1
    treeEncounters = 0
    pivot = 0
    for index, line in enumerate(parameters['input']):
        row = []
        for i in range(0, repeats):
            row.extend(line)

        if down == 1:
            print (f"({index, pivot})")
            if index > 0 and row[pivot] == '#':
                treeEncounters += 1
            pivot += right

        if down == 2 and index % down == 0:
            print (f"({index, pivot})")
            if row[pivot] == '#':
                treeEncounters += 1
            pivot += right

    print(f"- Right {right}, down {down}. Trees encountered {treeEncounters}")
    return treeEncounters

treeEncountersSlope1 = getTreeEncounters(1, 1)
treeEncountersSlope3 = getTreeEncounters(3, 1)
treeEncountersSlope5 = getTreeEncounters(5, 1)
treeEncountersSlope7 = getTreeEncounters(7, 1)
treeEncountersSlope12 = getTreeEncounters(1, 2)

result = treeEncountersSlope1 * treeEncountersSlope3 * treeEncountersSlope5 * treeEncountersSlope7 * treeEncountersSlope12
print(result)