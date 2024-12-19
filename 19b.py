from ast import iter_fields
from ctypes.wintypes import tagPOINT
from pydoc_data.topics import topics

lines = open("19.txt").read().splitlines()
towels = lines[0].replace(" ","").split(",")
patterns = lines[2:]
cache = {"":1}

def match(pat):
    if pat in cache:
        return cache[pat]

    ant = sum([match(pat[len(t):]) for t in towels if t == pat[0:len(t)]])
    cache[pat] = ant
    return ant

print(sum([match(p) for p in patterns]))