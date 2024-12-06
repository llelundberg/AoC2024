lines = open("02.txt").read().splitlines()

def testa(report):
    step = 0
    for i in range(0,len(report)-1):
        a = report[i]
        b = report[i+1]
        if a>b:
            if step == 0:
                step = -1
            if step > 0:
                return "unsafe"
        if a<b:
            if step == 0:
                step = 1
            if step < 0:
                return "unsafe"
        if(abs(a-b)>3 or a==b ):
            return "unsafe"
    return "safe"

ant=0
for line in lines:
    report = [int(x) for x in line.split()]
    print(report)
    status = "unsafe"
    for i in range(0,len(report)):
        r = [report[j] for j in range(0,len(report)) if i!=j ]
        print ("* ", r)
        status = testa(r)
        if status == "safe":
            break
    print(report, status)

    if status == "safe":
       ant += 1

print(ant)

