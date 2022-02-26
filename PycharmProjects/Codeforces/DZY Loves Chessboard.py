n, m = list(map(int, input().split()))
arr100 = []
'''for kk in range(jkj):
    arr1000.append([])'''
for _ in range(n):
    arr100.append([])
    #arr1000.append(arr10)
    #print(arr1000)
    arr = list(map(str, list(input())))
    #print(lis)
    for k in range(m):
        #print(_, k)
        if arr[k] == '-':
            arr100[_].append('-')
        else:
            if _ % 2 == 0:
                if k % 2 == 0:
                    arr100[_].append('B')
                else:
                    arr100[_].append('w')
            else:
                if k % 2 == 0:
                    arr100[_].append('w')
                else:
                    arr100[_].append('B')
    print(''.join(arr100[_]))
#print(arr1000)

