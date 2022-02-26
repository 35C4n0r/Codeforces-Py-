# cook your dish here
s = input()
arr = list(s)
print(arr)
arr2 = []
for k in range(len(arr)):
    if arr[k] == '+':
        for _ in range(int(arr[k-1])):
            arr2.append("".join(arr[k + 1 : arr.index('-')]))
            print(arr2)
    if arr[k] == '-':
        arr2.append(arr[arr[k+1] : arr])