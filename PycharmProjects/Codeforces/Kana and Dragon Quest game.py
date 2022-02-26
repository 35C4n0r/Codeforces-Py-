# 900
for _ in range(int(input())):
    h, a, b = list(map(int, input().split()))
    count = 0
    if b == 0:
        print("NO")
    elif b * 10 >= h:
        print("YES")
    else:
        z = b * 10
        while h > z:
            h = (h//2 + 10)
            count += 1
            if count > a:
                print("NO")
                break
        if count <= a:
            print("YES")

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
