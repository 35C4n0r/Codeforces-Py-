for _ in range(int(input())):
    n = int(input())
    count = 0
    arr = list(map(int, input().split()))
    arr2020 = set(arr)
    if len(arr2020) == 1 and arr2020 == {1}:
        z = arr.count(1)
        if z%2 == 0:
            print("Second")
        else:
            print("First")
    elif 1 not in arr:
        print("First")
    else:
        if arr[0] == 1:
            for k in arr:
                if k == 1:
                    count += 1
                    if count%2 != 0:
                        ans = "Second"
                    else:
                        ans = "First"
                else:
                    print(ans)
                    break
        else:
            print("First")
