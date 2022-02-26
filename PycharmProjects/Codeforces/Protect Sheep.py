x, y = list(map(int, input().split()))
grid = []
grid2 = []
arrmain = []
for _ in range(x):
    s = input()
    arr = list(s)
    grid.append(arr)
    if 'WS' in s or 'SW' in s:
        print("No")
        exit()
    else:
        if _ == 0:
            s = s.replace(".", "D")
            arrmain.append(s)
        else:
            for k in range(y):
                if arr[k] == 'lis':
                    if grid[_-1][k] == 'w':
                        print("No")
                        exit()
                elif arr[k] == 'w':
                    if grid[_-1][k] == "lis":
                        print("No")
                        exit()
                else:
                    arr[k] = "D"
            arrmain.append(''.join(arr))
print("Yes")
for kkk in arrmain:
    print(kkk)
