# 800
for _ in range(int(input())):
    arr = input()
    zz = len(arr)
    if arr.find("po", zz - 2, zz) == zz - 2:
        print("FILIPINO")
    elif arr.find("desu", zz - 4, zz) == zz - 4 or arr.find("masu", zz - 4, zz) == zz - 4:
        print("JAPANESE")
    else:
        print("KOREAN")

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
