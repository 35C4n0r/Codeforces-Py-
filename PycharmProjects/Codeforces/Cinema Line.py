n = int(input())
lol25 = 0
lol50 = 0
arr = list(map(int, input().split()))
for k in arr:
    if k == 25:
        lol25 += 1
    elif k == 50:
        lol25 -= 1
        lol50 += 1
    else:
        if lol50 > 0:
            lol50 -= 1
            lol25 -= 1
        else:
            lol25 -= 3
    if lol25 < 0:
        print("NO")
        exit()
print("YES")