n = int(input())
s = input()
arr = list(s)
x = 0
y = 0
xa, ya = list(map(int, input().split()))
for k in arr:
    if k == 'U':
        y += 1
    elif k == 'D':
        y -= 1
    elif k == 'L':
        x -= 1
    else:
        x += 1
#print(x, y)
print(abs(x - xa) + abs(y - ya))