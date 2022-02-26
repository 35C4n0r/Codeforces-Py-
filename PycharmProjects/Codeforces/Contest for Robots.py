n = int(input())
arrb = [0] * n
count = 0
arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
'''for k in range(jkj):
    if arr1000[k] == 1:
        arrb[k] += 1
gg = sum(arrb)'''
for a, b in zip(arr, arr2):
    if a == 1 and b == 0:
        count += 1
if count == 0 and sum(arr2) >= sum(arr):
    print("-1")
    exit()

if sum(arr) == count:
    ab = sum(arr2) + 1
    if ab % count == 0:
        f = ab // count
    else:
        f = (ab // count) + 1
    print(f)
elif sum(arr) > sum(arr2):
    print(1)
elif sum(arr) == sum(arr2):
    print(2)
else:
    ab = sum(arr2) - sum(arr) + count
    if ab % count == 0:
        f = ab // count
    else:
        f = (ab // count) + 1
    print(f)

#                        _
#  _._ _..._ .-',     _.._(`))
# '-. `     '  /-._.-'    ',/
#   )         \            '.
#  / _    _    |             \
# |  arr    arr    /              |
# \   .-.                     ;
#  '-('' ).-'       ,'       ;
#     '-;           |      .'
#        \           \    /
#        | 7  .__  _.-\   \
#        | |  |  ``/  /`  /
#       /,_|  |   /,_/   /
#          /,_/      '`-'

