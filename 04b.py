m = open("04.txt").read().splitlines()

ant = 0
for r in range(1,len(m)-1):
    for c in range(1,len(m[r])-1):
        w1 = m[r-1][c-1] + m[r][c] + m[r+1][c+1]
        w2 = m[r-1][c+1] + m[r][c] + m[r+1][c-1]
        ant += w1 in ("MAS","SAM") and w2 in ("MAS","SAM")

print(ant)

