for _ in range(int(input())):
    n = int(input())
    arr = input()
    count = 0
    for k in range(n):
        if "()" in arr:
            arr = arr.replace("()", "", 1)
            count += 1
        else:
            break
    print((n - count * 2) // 2)

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
