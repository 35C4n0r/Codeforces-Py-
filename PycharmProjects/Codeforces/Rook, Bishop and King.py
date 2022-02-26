bx, by, ex, ey = list(map(int, input().split()))
arr = []
if bx == ex or by == ey:
    print(1, end=" ")
else:
    print(2, end=" ")
if (bx + by) % 2 == (ex + ey) % 2:
    if bx + by == ex + ey or bx - by == ex - ey:
        print(1, end=' ')
    else:
        print(2, end=' ')
else:
    print(0, end=' ')
print(max((abs((bx - ex))), (abs(by - ey))))