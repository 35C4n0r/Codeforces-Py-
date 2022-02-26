# 900
for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    c, d = list(map(int, input().split()))
    if (a == c and b + d == a) or (b == c and a + d == b) or (a == d and b + c == a) or (b == d and a + c == d):
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


