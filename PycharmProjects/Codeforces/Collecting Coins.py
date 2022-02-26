# 800
for _ in range(int(input())):
    a, b, c, n = list(map(int, input().split()))
    z = max(a, b, c)
    sum = (z - a) + (z - b) + (z - c)
    if (n - sum) % 3 == 0 and n >= sum:
        print("Yes")
    else:
        print("No")

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
