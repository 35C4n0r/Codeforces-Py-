count = 0
for _ in range(int(input())):
    s = input()
    if '+' in s:
        count += 1
    else:
        count -= 1
print(count)