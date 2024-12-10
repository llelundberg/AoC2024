lines = open("10test.txt").read().splitlines()

for line in lines:
    print(line)

m={}
for r in range(0,len(lines)):
    for c in range(0,len(lines[r])):
        if lines[r][c]>="0" and lines[r][c]<="9":
            m[(r,c)] = int(lines[r][c])

print("m",m)


def recurse(pos):
    h = m[pos]
    if h==9:
        return 1
    ret = 0
    r,c = pos
    for rr, cc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
        if (rr,cc) in map and m[(rr,cc)]==h+1:
            ret += 1+recurse((rr,cc))
    return ret

heads = [(r,c) for (r,c) in m if m[(r,c)]==0]
scores = []
print("heads",len(heads),heads)
for h in heads:
    q = [h]
    trail = {}
    while len(q)>0:
        (r,c) = q.pop()
        h = m[(r,c)]
        trail[(r,c)] = []
        #print("neighbours of",(r,c), h)
        for rr, cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)]:
            #print("  ", (rr, cc))
            if (rr,cc) in m and (rr,cc) not in trail and (rr,cc) not in q:
                #print("    ", (rr, cc))
                if m[(rr,cc)]==h+1:
                    q.append((rr,cc))
        #print(len(trail),trail)

    print(trail)
    score = sum([ 1 for v in trail.values() if v == 9])
    scores.append(score)
print("scores",scores)
print(sum(scores))