# cook your dish here
n, h = list(map(int, input().split()))
arri = list(map(int, input().split()))
arr = list(map(int, input().split()))
hold = False
right = 0
for k in arr:
    if k == 1 and right != 0:
        right -= 1
    elif k == 2 and right < n - 1:
        right += 1
    elif k == 3 and hold is False and arri[right] > 0:
        hold = True
        arri[right] -= 1
    elif k == 4 and hold is True and arri[right] < h:
        hold = False
        arri[right] += 1
    elif k == 0:
        print(*arri)
