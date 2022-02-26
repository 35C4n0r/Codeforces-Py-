for _ in range(int(input())):
    truth_list = []
    arr = []
    arr2 = []
    r, c = list(map(int, input().split()))
    for q in range(r):
        w = input().split()
        arr.append(w)
    rr, cc = list(map(int, input().split()))
    for e in range(rr):
        t = input()
        arr2.append(t)
    for o in range(len(arr)):
        m = arr2[0]
        if m in arr[o][0]:
            z = arr[o][0].index(arr2[0])
            y = o
            arr2.pop(0)
            break
    for d, f in zip(range(o + 1, o + rr), arr2):
        if f in arr[d][0] and arr[d][0].index(f) == z:
            truth_list.append(1)

    if len(truth_list) == rr - 1:
        print("YES")
    else:
        print("NO")