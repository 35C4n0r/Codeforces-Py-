n = input()
arr = list(map(int, list(n)))
z = sum(arr)
if z % 3 == 0:
    print(0)
else:
    if z <= 2:
        print(-1)
        exit()
    smh = z % 3
    if smh in arr:
        print(1)
    else:
        print(2)
