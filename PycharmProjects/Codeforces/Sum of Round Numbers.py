for _ in range(int(input())):
    n = input()
    arr = list(map(str, list(n)))
    z = len(arr)
    print(z - arr.count('0'))
    for k in range(z):
        result = []
        if arr[k] != '0':
            result.append(arr[k])
            result.append(''.join(['0']*(z-(k+1))))
            print(''.join(result), end=' ')
    print()


