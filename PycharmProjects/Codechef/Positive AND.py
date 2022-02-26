import math
for _ in range(int(input())):
    n = int(input())
    arr = [2, 3, 1]
    post = 0
    if n != 1:
        if math.log(n, 2) != int(math.log(n, 2)):
            for j in range(4, n+1):
                if j == 1 or math.log(j, 2) != int(math.log(j, 2)):
                    arr.append(j)
                    if post != 0:
                        arr.append(post)
                        post = 0
                else:
                    post = j
            print(*arr)
        else:
            print(-1)
        #for k in range(n - 1):
            #print(arr[k]&arr[k+1])
    else:
        print(n)
