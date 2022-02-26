n = input()
arr = list(map(str, list(str(int(n) + 1))))
n = int(n)

while len(arr) != len(set(arr)):
    n += 1
    arr = list(map(str, list(str(int(n) + 1))))
else:
    print(''.join(arr))
