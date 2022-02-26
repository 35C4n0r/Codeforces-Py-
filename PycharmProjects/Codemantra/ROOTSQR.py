import math
result = []
tc, x = list(map(int, input().split()))
for _ in range(tc):
    number = int(input())
    if number < 0:
        print("no")
    else:
        s = int(math.sqrt(number))
        diff = number - (s ** 2)
        if diff <= (x / 100) * number:
            print("yes")
        else:
            print("no")
