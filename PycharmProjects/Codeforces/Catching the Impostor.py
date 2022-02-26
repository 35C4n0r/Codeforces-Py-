n, k = list(map(int, input().split()))
arr = list(map(int, input().split()))
if n - len(set(arr)) == 1:
    print("YES")
else:
    print("NO")
