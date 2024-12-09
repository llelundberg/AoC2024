data = open("09.txt").read()

files = {}
spaces = {}

# Parse the input into files and spaces
fid = 0
sid = 0
pos = 0
isFile = True
for i in range(0,len(data)):
    l = int(data[i])   # Siffran i input
    seg = (pos,l)      # Segmentet är en startposition och en längd

    if isFile:
        files[fid] = seg
        fid += 1
    else:
        spaces[sid] = seg
        sid += 1

    pos = pos + l
    i +=1
    isFile = not isFile

#print(files)
#print(spaces)

# Traverserar filerna i omvänd ID-ordning
for fid in range(max(files),-1,-1):
    # filens nuvarande position och längd
    fp, fl = files[fid]

    # Filtrerar ut alla tomrum där filen skulle få plats
    poss_spaces = [sid for sid,(sp,sl) in spaces.items() if sp < fp and sl>=fl ]

    # Om det går att flytta filen (finns ett tomrum där filen ryms)
    if len(poss_spaces)>0:
        sid = poss_spaces[0]                # Flytta till första möjliga tomrum
        sp, sl = spaces[sid]                # Position och längd för tomrummet
        files[fid] = (sp, fl)               # Flyttar filen
        spaces[sid] = (sp + fl , sl - fl)   # Minskar tomrummet

# Beräknar checksumman
checksum = 0
for fid in files:
    fp,fl = files[fid]
    for i in range(fp,fp+fl):
        checksum += i * fid

print(checksum)

