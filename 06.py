import time
start_time = time.time()

lines = open("06.txt").read().splitlines()
dir = [(-1, 0), (0, 1), (1, 0), (0, -1)]

maze = {}
for r in range(0, len(lines)):
    for c in range(0, len(lines[r])):
        maze[(r, c)] = lines[r][c]
        if maze[(r, c)] == "^":
            start_r, start_c = (r, c)

def solve_maze():
    r, c = start_r, start_c
    d = 0
    dr,dc = dir[d]
    visited = {}
    while (r,c) in maze:
        if (r,c) not in visited:
            visited[(r, c)] = []

        if d in visited[(r,c)]:
            return True,visited

        visited[(r, c)].append(d)

        if (r+dr, c+dc) in maze and maze[(r + dr, c + dc)] == "#":
            d = (d+1) % len(dir)
            (dr,dc) = dir[d]
        else:
            (r,c) = (r+dr, c+dc)

    return False,visited



_, path = solve_maze()
print("Del 1:",len(path))

ant = 0
for (r,c) in list(path.keys()):
    maze[(r, c)]= "#"
    res,_ = solve_maze()
    maze[(r, c)] = "."
    if res:
        ant+=1

print("Del 2:",ant)

print("--- %s seconds ---" % (time.time() - start_time))













