lines = open("07.txt").read().replace(":","").splitlines()


def evaluate(goal,val,numbers):
    if len(numbers)==0:
        return val == goal

    if val>goal:
        return False

    if evaluate(goal,val*numbers[0],numbers[1:]):
        return True
    if evaluate(goal,val+numbers[0],numbers[1:]):
        return True

    # Avkommentera för uppgift 2
    if evaluate(goal,int(str(val) + str(numbers[0])),numbers[1:]):
        return True

    return False

valid = []
for line in lines:
    a = [int(x) for x in line.split()]
    if evaluate( a[0], a[1], a[2:]):
        valid.append(a[0])

print(sum(valid))