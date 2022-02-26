lol = {}
arr = []
for _ in range(int(input())):
    k = input()
    arr.append(k)
if len(set(arr)) == 1:
    print(*arr)
else:
    arr2 = list(set(arr))
    if arr.count(arr2[0]) > arr.count(arr2[1]):
        print(arr2[0])
    else:
        print(arr[1])