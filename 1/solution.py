import numpy
import sys
import json

parameters = json.load(open("input.json", "r"))

def discoverGroups(depth, limit, entries):
    groups = []
    if depth == 1 : return [[limit] if limit in entries else groups]
    for e in entries:
        if e >= limit/depth and e <= limit:
            groups.extend([s + [e] for s in discoverGroups(depth-1, limit-e, [n for n in entries if n < e])])
    return groups

print(max([numpy.prod(e) for e in discoverGroups(parameters['depth'], parameters['limit'], parameters['entries']) if len(e) == parameters['depth']]))