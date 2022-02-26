n = int(input())
phi = 1.6180339
count = 5
arr = [0, 1, 1, 2, 3, 5]
fn = 5
def round_int(x):
    if x == float("inf") or x == float("-inf"):
        return float('nan') # or x or return whatever makes sense
    return int(round(x))
if n == 0:
    print(0, 0, 0)
elif n == 1:
    print(0, 0, 1)
elif n == 2:
    print(0, 1, 1)
elif n == 3:
    print(0, 1, 2)
elif n == 5:
    print(0, 2, 3)
else:
    while fn != n:
        count += 1
        fn = arr[count - 1] + arr[count - 2]              #round_int(phi * fn)
        arr.append(fn)
    else:
        print(arr[count - 1], arr[count - 3], arr[count - 4])
        exit()
