lines = open("01.txt").read().splitlines()

# Skapar en höger och vänster-lista
l = []
r = []
for line in lines:
    x = line.split()
    l.append(int(x[0]))
    r.append(int(x[1]))

# Sorterar listorna
l.sort()
r.sort()

# Beräknar skillnaden mellan varje talpar, och summerar skillnaden
print(sum([abs(l[i] - r[i]) for i in range(0,len(r))]))

# Räknar förekomster i högra listan för varje tal i vänstra listan
print(sum([i * len([j for j in r if j==i]) for i in l]))
