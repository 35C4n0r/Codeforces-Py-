a, b, n = list(map(int, input().split()))
arr = [str(a)]
x = a
for _ in range(1):
    x = int(f'{x}{9}')
    smh = x % b
    if smh <= 9:
        x -= smh
    else:
        print(-1)
        exit()
arr2 = ['0']*(n-1)
arr2.insert(0, str(x))
print(''.join(arr2))