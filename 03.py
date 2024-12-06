import re
text = open("03.txt").read()
matches = re.findall("mul\\([0-9]+,[0-9]+\\)|do\\(\\)|don't\\(\\)",text)

s = 0
status = True
for m in matches:
    print(m)
    if m == "do()":
        status = True
    elif m == "don't()":
        status = False
    elif status:
        digits = m.replace("("," ").replace(","," ").replace(")","").split()
        s += (int(digits[1]) * int(digits[2]))
print(s)