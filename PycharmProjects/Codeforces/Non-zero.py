# 800
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    z = arr.count(0)
    for _ in range(z):
        arr.remove(0)
        arr.append(1)
    count = 0
    count += z
    if sum(arr) != 0:
        print(count)
    else:
        print(count + 1)

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
