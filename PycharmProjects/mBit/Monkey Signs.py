s = input()
s = s.lower()
#print(s)
arr = list(s)
mm = 0
co = 0
arr2 = list(set(arr))
for k in arr2:
    if k != 'm':
        co = max(co, arr.count(k))
print(arr.count('m') + co)