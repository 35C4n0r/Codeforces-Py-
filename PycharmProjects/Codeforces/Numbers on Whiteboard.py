import math
for _ in range(int(input())):
    n = int(input())
    a = [k for k in range(1, n+1)]
    a.reverse()
    #print(arr)
    print(2)
    second_thread = a[0]
    for k in range(1, n):
        print(second_thread, a[k])
        second_thread += a[k]
        second_thread = math.ceil(second_thread/2)


