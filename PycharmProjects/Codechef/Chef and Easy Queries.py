# cook your dish here
import math
for _ in range(int(input())):
    pre = False
    current = 0
    post = 0
    n, k = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    for j in arr:
        if post + j >= k:
            post += j - k
            current += 1
        else:
            print(current+1)
            pre = True
            # print(post)
            break

    if not pre:
        #print(post)
        current += post // k
        print(current + 1)
