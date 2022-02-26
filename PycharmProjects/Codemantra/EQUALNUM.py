result = []
for _ in range(int(input())):
    w, i = list(map(str, input().split()))
    international = w.replace(",", "")
    local = i.replace(",", "")
    if int(international) == int(local):
        result.append("equal")
    else:
        result.append("different")
for k in result:
    print(k)
