lines = open("02.txt").read().splitlines()
ant=0
for line in lines:
    report = [int(x) for x in line.split()]
    step = 0
    status = "safe"
    for i in range(0,len(report)-1):
        a = report[i]
        b = report[i+1]
        if a>b:
            if step == 0:
                step = -1
            if step > 0:
                status ="unsafe"
        if a<b:
            if step == 0:
                step = 1
            if step < 0:
                status ="unsafe"
        if(abs(a-b)>3 or a==b ):
            status = "unsafe"
    print(report, status)
    if status == "safe":
        ant +=1

print(ant)

