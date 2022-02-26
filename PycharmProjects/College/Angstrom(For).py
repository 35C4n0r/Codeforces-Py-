n = int(input())
counter = 0
while counter < n+1:
    s = str(counter)
    arr = list(map(int, list(s)))
    dig_sum = 0
    for j in arr:
        dig_sum += j**len(arr)
    if dig_sum == counter:
        print(counter)
    counter += 1
