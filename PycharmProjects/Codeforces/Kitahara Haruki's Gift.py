n = int(input())
arr = list(map(int, input().split()))
z = sum(arr) // 2
if z % 100 == 0 and z % 200 == 0:
    print("YES")
else:
    print("NO")
