from sys import *
input = stdin.readline
for _ in range(int(input())):
    a = int(input())
    arr = list(map(int, list(str(a))))
    arr2 = arr.copy()
    ind = len(arr) - 1
    for i in range(len(arr) - 1):
        #print(i)
        if arr[i] > arr2[i + 1]:
            ind = i
            break
    arr2.pop(ind)
    arr2 = list(map(str, arr2))
    print(int(''.join(arr2)))