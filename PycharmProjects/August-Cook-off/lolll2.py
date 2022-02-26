for _ in range(int(input())):
    n = int(input())
    k = list(input())
    arr = list(map(int, k))
    a = arr[n - 1]
    b = [a]*n
    z = map(str, b)
    string = "".join(z)
    print(string)