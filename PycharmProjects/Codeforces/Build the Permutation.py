# Based on the fact that set cannot have duplicates
arr = list(map(int, input().split()))
arr2 = set()
for k in arr:
    arr2.add(k)
print(*arr2)

# Alternate

"""
arr = list(map(int, input().split()))
arr2 = set(arr)
print(*arr)
"""
