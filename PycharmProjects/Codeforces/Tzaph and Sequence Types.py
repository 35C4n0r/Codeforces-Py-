n = int(input())
arr = list(map(int, input().split()))
if len(set(arr)) == 1:
    print("EQUAL")
elif arr == sorted(arr):
    print("NONDECREASING")
elif arr == sorted(arr, reverse=True):
    print("NONINCREASING")
else:
    print("NONE")
