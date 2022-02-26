n = int(input())
ax, ay = list(map(int, input().split()))
bx, by = list(map(int, input().split()))
cx, cy = list(map(int, input().split()))
mithoo = False
if bx < ax and by < ay:
    if cx < ax and cy < ay:
        mithoo = True
elif bx > ax and by < ay:
    if cx > ax and cy < ay:
        mithoo = True
elif bx > ax and by > ay:
    if cx > ax and cy > ay:
        mithoo = True
elif bx < ax and by > ay:
    if cx < ax and cy > ay:
        mithoo = True
if mithoo:
    print("YES")
else:
    print("NO")

