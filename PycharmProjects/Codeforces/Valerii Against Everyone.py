from collections import Counter
'''def divideArray(arr2, n):
    sem = sum(arr2)
    left_sum = 0
    left_sem = 0
    for i in range(n):
        left_sem += arr2[i]
        right_sum = sem - left_sum - arr2[i]
        if left_sem - right_sum == 0:
            return True
        left_sum += arr2[i]
    return False

for _ in range(int(input())):
    n = int(input())
    arr2 = []
    arrjj = list(map(int, input().split()))
    for k in arrjj:
        arr2.append(2**k)
    #print(arr2)
    if divideArray(arr2, n) == True:
        print("YES")
    else:
        print("NO")'''
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    if len(set(arr)) != n:
        print("YES")
    else:
        print("NO")