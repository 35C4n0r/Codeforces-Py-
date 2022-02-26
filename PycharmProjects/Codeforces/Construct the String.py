# 900
for _ in range(int(input())):
    n, a, b = list(map(int, input().split()))
    alpha_in = "abcdefghijklmnopqrstuvwxyz"
    arr3 = list(alpha_in)
    result = []
    for i in range(n):
        result.append(arr3[i % b])
    print("".join(result))

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

