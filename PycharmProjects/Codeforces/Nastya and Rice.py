# 900
for _ in range(int(input())):
    n, a, b, c, d = list(map(int, input().split()))
    ul = a + b
    ll = abs(b - a)
    uul = c + d
    ull = abs(d - c)
    if ull <= ul * n <= uul or ull <= ll * n <= uul or ll <= uul <= ul or ll <= ull <= ul:
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
