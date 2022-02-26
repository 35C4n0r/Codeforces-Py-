n = input()
arr = list(map(int, list(n)))
arr2 = set(arr)
if len(arr2) == 2:
    if arr2 == {4, 7} or arr2 == {7, 4}:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
