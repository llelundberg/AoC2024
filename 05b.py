text = open("05x.txt").read().replace("\n\n", "¤")

rules = []
updates = []
for x in text.split("¤")[0].splitlines():
    rules.append((int(x.split("|")[0]), int(x.split("|")[1])))
for x in text.split("¤")[1].splitlines():
    updates.append([int(xx) for xx in x.split(",") ])

middle=[]
for update in updates:

    # För varje tal i lista, kolla vilka andra tal i listan som är FÖRE talet.
    before = {}
    for item in update:
        before[item] = [b for (b,a) in rules if a == item and b in update]

    # Skapa en sorterad kopia av uppdateringen.
    sorted_up = []
    while len(before)>0:
        # Det ska bara vara ETT tal i listan som INTE har några andra tal framför sig.
        # Denna har en TOM före-lista.
        first = [k for k,v in before.items() if len(v)==0]
        assert(len(first)==1)
        sorted_up.append(first[0])

        # Raderar talet som ska vara först från alla kvarvarande listor.
        del before[first[0]]
        for k,v in before.items():
            v.remove(first[0])

    # Om uppdateringen skiljer sig från ursprungliga uppdateringen
    if update != sorted_up:
        middle.append(sorted_up[int(len(sorted_up)/2)])

print(sum(middle))
