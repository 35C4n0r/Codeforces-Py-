arr = list(input())
arr2 = list(input())
arr100 = []
for k, kk in zip(arr, arr2):
    if k == kk:
        arr100.append("0")
    else:
        arr100.append("1")
print("".join(arr100))