n = int(input())
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
ans = 0
for k in range(n-1, -1, -1):
    cunt = 0
    z = arr[-1]
    arr.pop(-1)
    arr.insert(0, z)
    for gg, ggg in zip(arr, arr2):
        if gg == ggg:
            cunt += 1
    ans = max(ans, cunt)
print(ans)