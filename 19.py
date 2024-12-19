lines = open("19.txt").read().splitlines()

towels = lines[0].replace(" ","").split(",")
patterns = lines[2:]

def match(pat,towels):
    if pat == "":
        return True

    towels2 = [t for t in towels if t in pat]
    #print(len(towels),len(towels2))
    for t in towels2:
        if pat.startswith(t):
            if match(pat[len(t):],towels2):
                return True

    return False

result = []
#for pat in patterns:
#    print(pat)
#    result.append(match(pat,towels))


possible = []
for pat in patterns:
    print(pat)
    matches = [ [] for p in pat]

    for t in towels:
        #print("towel:",t)
        for i in range(0,len(pat)-len(t)+1):
            subpat = pat[i:i+len(t)]
            if t==subpat:
                #print(" ",t,"matchar i position",i)
                for j in range(i,i+len(t)):
                    matches[j].append((i,t))



    for i in range(len(pat)):
        print(i,pat[i],matches[i])
    possible.append(sum([1 for m in matches if len(m)==0])==0)

print(sum(possible))

