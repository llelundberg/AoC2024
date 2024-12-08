import itertools

lines = open("08.txt").read().splitlines()

max_r, max_c = len(lines), len(lines[0])

antennas = {}
for r in range(0,max_r):
    for c in range(0, max_c):
        a = lines[r][c]
        if a != ".":
            if a not in antennas:
                antennas[a] = []
            antennas[a].append((r,c))

antinodes = set()

for a in antennas:
    for ((r1,c1),(r2,c2)) in itertools.combinations(antennas[a],2):

        dr, dc = abs(r1-r2), abs(c1-c2)

        # antinode 1
        ar = r1-dr if r1<r2 else r1+dr
        ac = c1-dc if c1<c2 else c1+dc
        antinodes.add((ar,ac))

        # antinode 2
        ar = r2-dr if r2<r1 else r2+dr
        ac = c2-dc if c2<c1 else c2+dc
        antinodes.add((ar,ac))

# Filtrera bort de som ligger utanför kartan
antinodes= [ (r,c) for (r,c) in antinodes if 0<=r<max_r and 0<=c<max_c]

print(len(antinodes))


