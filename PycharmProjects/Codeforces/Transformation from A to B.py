a, b = list(map(int, input().split()))
ans = [b]
flag = False
while a != b:
    "1"
    arr = list(str(b))
    if arr[-1] == "1":
        arr.pop(-1)
        b = int("".join(arr))
        ans.append(b)
    elif b % 2 == 0:
        ans. append(b // 2)
        b = b//2
    if a == b:
        break
    if b < a or (int(arr[-1])%2 != 0 and arr[-1] != "1"):
        flag = True
        break
if not flag:
    print("YES")
    ans.reverse()
    print(len(ans))
    print(*ans)
else:
    print("NO")
    #print(ans)