n = int(input())
arr = []
for k in range(n, 0, -1):
    arr.append(k)
if sum(arr) % 2 != 0:
    print("NO")
    exit()
print("YES")
A = []
B = []
sum_A = 0
sum_B = 0
for n in arr:
    if sum_A < sum_B:
       A.append(n)
       sum_A = sum_A + n
    else:
       B.append(n)
       sum_B = sum_B + n
print(len(A))
for h in A:
    print(h, end=" ")
print()
print(len(B))
for l in B:
    print(l, end=" ")
