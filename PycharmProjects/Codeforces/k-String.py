n = int(input())
s = input()
arr = list(s)
arr10 = []
if n == 1:
    print(s)
else:
    for k in set(arr):
        xy = arr.count(k)
        if xy % n != 0:
            print(-1)
            exit()
        else:
            arr10.append(k*(xy // n))
    se = ''.join(arr10)
    for _ in range(n):
        print(se, end='')