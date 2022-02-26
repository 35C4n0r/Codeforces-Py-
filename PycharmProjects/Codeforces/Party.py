arr = {}
for _ in range(int(input())):
    n = int(input())

    if n not in arr:
        arr[n] = [_ + 1]
    else:
        arr[n].append(_ + 1)
print(arr)