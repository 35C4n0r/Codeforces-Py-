# 900
for _ in range(int(input())):
    count = 0
    a, b, c, d = list(map(int, input().split()))
    sleep = b
    total = b
    if b >= a:
        print(b)
    elif d >= c:
        print(-1)
    else:
        zz = a - b
        count = zz // (c - d)
        if zz % (c - d) != 0:
            count += 1
        total += c * count
        print(total)

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
