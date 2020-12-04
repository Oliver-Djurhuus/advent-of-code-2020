import sys
import json

para = json.load(open("input.json", "r"))

es = []
for e in para["input"]:
    es.append( [int(e.split('-')[0]), int(e.split('-')[1].split(' ')[0]), e.split(' ')[1].split(':')[0], e.split(': ')[1], False])

# Assignment 1
result1 = 0
for e in es:
    occurences = e[3].count(e[2])
    print(f'{occurences} - {e}')
    if occurences >= e[0] and occurences <= e[1]:
        e[4] = True
        result1 += 1

print(result1)


# Assignment 2
result2 = 0

def valid(position, letter, password):
    position -= 1
    if position >= 0 and position < len(password):
        if password[position] == letter:
            print(True)
            return True
        else:
            print(False)
            return False
    return False

for e in es:
    if valid(e[0], e[2], e[3]) != valid(e[1], e[2], e[3]):
        result2 += 1

print(result2)