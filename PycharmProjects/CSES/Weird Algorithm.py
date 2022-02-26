n = int(input())
arr = []
while n > 1:
    arr.append(n)
    if n % 2 == 0:
        n //= 2
    else:
        n *= 3
        n += 1
arr.insert(len(arr), 1)
for j in arr:
    print(j, end=" ")









