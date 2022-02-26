s = input()
s = s.replace(' ', '')
arr = list(s)
j = input()
j = j.replace(" ", '')
arr2 = list(j)
for k in arr2:
    if k in arr:
        arr.remove(k)
    else:
        print("NO")
        exit()
print("YES")