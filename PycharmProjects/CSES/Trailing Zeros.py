n = int(input())
arr = []
while n >= 5 :
    n //= 5
    arr.append(n)
print(sum(arr))


