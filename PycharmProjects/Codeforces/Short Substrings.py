for _ in range(int(input())):
    s = input()
    arr = list(s)
    for k in range(2, len(s) - 1, 2):
        arr.pop(k)
        arr.insert(k, " ")
    j = ''.join(arr)
    j = j.replace(" ", '')
    print(j)