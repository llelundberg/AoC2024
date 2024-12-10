import itertools

f = open("10.txt").read().splitlines()

m={ (r,c): int(f[r][c]) for r,c in itertools.product(range(len(f)),range(len(f[0]))) }

def recurse(r,c):
    return 1 if m[(r,c)]==9 else sum([recurse(rr,cc) for rr,cc in [(r+1,c),(r-1,c),(r,c+1),(r,c-1)] if (rr,cc) in m and m[(rr,cc)]==m[(r,c)]+1])

print(sum([recurse(r,c) for r,c in [(r,c) for (r,c) in m if m[(r,c)]==0]]))

