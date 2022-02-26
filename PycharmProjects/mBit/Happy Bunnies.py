a, b = list(map(int, input().split()))
count = 0
for k in range(a, b+1):
    smh = str(k)
    if '7' not in smh:
        count += k
        while k > 0:
            count += k % 10
            k //= 10
print(count)