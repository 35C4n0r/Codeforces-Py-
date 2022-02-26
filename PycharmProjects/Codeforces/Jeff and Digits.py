n = int(input())
arr = list(map(int, input().split()))
z = arr.count(5)
x = n - z
y = z % 9
arr.sort(reverse=True)
for _ in range(y):
    arr.remove(5)
#print(y, lis)
if len(arr) == 0 or x == 0:
    print(-1)
elif set(arr) == {0}:
    print(0)
else:
    arr = list(map(str, arr))
    print(''.join(arr))