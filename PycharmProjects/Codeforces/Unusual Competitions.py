n = int(input())
s = input()
arr = list(s)
count = 0
su = 0
p = -1
if n % 2 != 0:
    print(-1)
elif arr.count('(') != arr.count(')'):
    print(-1)
else:
    for k in range(n):
        if arr[k] == ')':
            count -= 1
        else:
            count += 1
        if count < 0 and p == -1:
            p = k
        elif count == 0 and p != -1:
            su += k - p + 1
            p = -1
    print(su)


