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

# Skapar en diskavbildning
disk_len = max([p+l for p,l in files.values()])
disk = [-1] * disk_len
#print(disk_len)

# Taggar varje block i disken med filens ID-nummer
for fid in files:
    fp,fl = files[fid]
    for i in range(fp,fp+fl):
        disk[i] = fid
#print(disk)

# Flyttar block på disken
head = 0
tail = len(disk)-1
while head<tail:
    while disk[head]>=0: head += 1
    while disk[tail]<0: tail -= 1
    if head>=tail:
        break
    disk[head] = disk[tail]
    disk[tail] = -1

#print(disk)

# Beräknar checksumman
checksum = 0
for i in range(0,len(disk)):
    if disk[i]>=0:
        checksum += i* disk[i]

print(checksum)


