text = open("05.txt").read().replace("\n\n","¤")

rules = []
updates = []
for x in text.split("¤")[0].splitlines():
    rules.append((int(x.split("|")[0]), int(x.split("|")[1])))
for x in text.split("¤")[1].splitlines():
    updates.append([int(xx) for xx in x.split(",") ])

middle = []
for up in updates:
    valid = True
    for i in range(0,len(up)):
        item = up[i]
        bef = up[0:i]
        aft = up[i+1:]
        #print(bef, item, aft)
        for b in bef:
            if (item,b) in rules:
                valid = False
        for a in aft:
            if (a,item) in rules:
                valid = False
    if valid:
        middle.append(up[int(len(up)/2)])

print(sum(middle))

