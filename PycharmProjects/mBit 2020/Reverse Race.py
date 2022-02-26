s = list(input())
#print(s)
s.reverse()
arr = ''.join(s).split()
#print(arr)
for k in arr:
    if k.lower() == k:
        print(k, end=' ')
    else:
        print(k.title(), end=' ')