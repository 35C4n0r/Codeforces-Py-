arr = [0, 1]
n = int(input())
counter = 2
while len(arr) < n:
    curr = arr[counter - 1] + arr[counter-2]
    arr.append(curr)
    counter += 1
print(*arr)