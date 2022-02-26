le = 0
re = 0
lo = 0
ro = 0
arr = []
for _ in range(int(input())):
    arr2 = []
    a, b = list(map(int, input().split()))
    if a%2 == 0:
        le += 1
        arr2.append("e")
    else:
        lo += 1
        arr2.append('o')
    if b%2 == 0:
        re += 1
        arr2.append('e')
    else:
        ro += 1
        arr2.append('o')
    arr.append(arr2)
#print(abcd)
if lo % 2 != 0 and ro % 2 == 0 or lo % 2 == 0 and ro % 2 != 0:
    print(-1)
elif lo % 2 != 0 and ro % 2 != 0:
    if ['e', 'o'] in arr or ['o', 'e'] in arr:
        print(1)
    else:
        print(-1)
else:
    print(0)