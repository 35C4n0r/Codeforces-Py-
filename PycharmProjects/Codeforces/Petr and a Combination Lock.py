arr = []
n = int(input())
for _ in range(n):
    arr.append(int(input()))
if sum(arr) == 360:
    print("YES")
    exit()
print(sum(arr))
arr.sort(reverse=True)
s = 0
ss = 0
real = 0
print(arr)
for k in arr:
    if s >= ss:
        ss += k
    else:
        s += k
print(s, ss, )
if s-ss == 0 or abs(s - ss) % 360 == 0:
    print("YES")
else:
    print("NO")