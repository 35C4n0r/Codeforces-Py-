n = int(input())
arr = list(map(int, input().split()))
x = min(arr)
if arr.count(x) > 1:
    print("Still Rozdil")
else:
    print(arr.index(x) + 1)