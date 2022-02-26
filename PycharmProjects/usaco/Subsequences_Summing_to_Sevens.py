fin = open('div7.in', 'r')
fout = open('div7.out', 'w')
n = int(fin.readline())
arr = [0]*n
arr2 = [-1]*7
for i in range(n):
    j = int(fin.readline())
    if i == 0:
        arr[0] = j
    else:
        arr[i] = arr[i-1] + j
for k in range(n):
    arr[k] %= 7
#dist = {}
#print(arr)
best = -1
for j, jj in enumerate(arr):
    #print(j, jj)
    if arr2[jj] == -1:
        arr2[jj] = j
    best = max(best, j - arr2[jj])
fout.write(str(best) + '\n')
fout.close()