
## Day #1

From a set of integers (entries) find the subset that sum to 2020 and has the highest product.

### Assignment 1 

The subset should be of 2 elements (```depth = 2```).

### Assignment 2:

The subset should be of 3 elements (```depth = 3```)


### General solution 

```python
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
```

[Download Solution](/solution.py)

[Settings](/input.json)


