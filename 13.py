
lines = open("13.txt").read().replace(","," ").replace("+"," ").replace("="," ").splitlines()
i = 0
cost = 0
while i < len(lines):
    ax,ay = int(lines[i].split()[3]),int(lines[i].split()[5])
    bx,by = int(lines[i + 1].split()[3]), int(lines[i + 1].split()[5])
    px, py = int(lines[i + 2].split()[2]), int(lines[i + 2].split()[4])
    #px, py = 10000000000000 + int(lines[i + 2].split()[2]), 10000000000000 + int(lines[i + 2].split()[4])

    a,r1 = divmod(px*by - py*bx,by*ax-bx*ay)
    b,r2 = divmod(px-ax*a,bx)

    if r1==0 and r2==0:
        cost += a*3+b

    i += 4

print("total cost",cost)