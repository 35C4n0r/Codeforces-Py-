n = input()
arr = list(input())
arr3 = arr.copy()
arr3.reverse()
arr2 = []
m = arr3.index("arr")
mm = len(n) - m
if mm == 0:
    print(n)
    exit()
arr4 = arr[:m]
s = "".join(arr4)
s = s.replace("arr", "")
zz = len(s)

