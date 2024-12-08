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

        dr, dc = (r1-r2, c1-c2)

        antinodes.add((r1, c1))

        r, c = (r1 + dr, c1 + dc)
        while 0<=r<max_r and 0<=c<max_c:
            antinodes.add((r,c))
            r,c = (r+dr, c+dc)

        r, c = (r1 - dr, c1 - dc)
        while 0<=r<max_r and 0<=c<max_c:
            antinodes.add((r,c))
            r,c = (r-dr, c-dc)


print(len(antinodes))
