
m = open("04.txt").read().splitlines()

ant = 0
for (dr, dc) in [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, 1), (1, -1), (-1, -1)]:
    for r in range((3 if dr<0 else 0),len(m)-(3 if dr>0 else 0)):
        for c in range((3 if dc<0 else 0),len(m[r])-(3 if dc>0 else 0)):
            if m[r][c] + m[r+dr][c+dc] + m[r+dr*2][c+dc*2] + m[r+dr*3][c+dc*3] == "XMAS":
                ant += 1

print(ant)

