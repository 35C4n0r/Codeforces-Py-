n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
arr.sort()
cunt = 0
t = 0
if len(arr) == 1 and arr[0] < 0:
    if k%2 != 0:
        print(abs(arr[0]))
    else:
        print(arr[0])
else:
    while t < min(n, k):
        if arr[t] < 0:
            arr[t] *= -1
            t += 1
        else:
            arr.sort()
            if (k-t) % 2 != 0:
                arr[0] *= -1
            break
    print(sum(arr))
    #print(abcd)