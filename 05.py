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
        # Delar upp uppdateringen i tre delar, talet, de som är före och de som är efter.
        item = up[i]
        bef = up[0:i]
        aft = up[i+1:]

        # Kontrollerar alla tal före att det inte finns någon regel som bryter mot detta.
        for b in bef:
            if (item,b) in rules:
                valid = False

        # Kontrollerar alla tal efter att det inte finns någon regel som bryter mot detta.
        for a in aft:
            if (a,item) in rules:
                valid = False
    if valid:
        middle.append(up[int(len(up)/2)])

print(sum(middle))

