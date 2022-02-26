n, p = list(map(int, input().split()))
arr = list(map(int, input().split()))
count = 0
co = 0
ce = 0
for k in arr:
    if k % 2 == 0:
        ce += 1
    else:
        co += 1
print(ce, co)
if p == 0:
    count += 2**ce + 2**co
else:
    count += 2 ** (ce + co)
print(count)
