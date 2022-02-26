n = int(input())
arr = []
result = []
if 1 < n <= 3:
    print("NO SOLUTION")
elif n == 1:
    print(1)
else:
    for k in range(2, n+1, 2):
        result.append(k)
    for f in range(1, n+1, 2):
        result.append(f)
for j in result:
    print(j, end=" ")








