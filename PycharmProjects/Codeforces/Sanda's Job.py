a, s = list(map(int, input().split()))
arr = list(map(int, list(str(a))))
arr2 = list(map(int, list(str(s))))
if a == s:
    print("NO")
elif s*2 == a:
    print("YES")
else:
    print(arr, arr2)