#
for _ in range(int(input())):
    n = int(input())
    arr = list(map(str, input().split()))
    word = "".join(arr)
    z = arr.count("0")
    zz = arr.count("1")
    if z >= zz:
        word = word.replace("1", "")
        print(len(word))
        for j in list(word):
            print(j, end=" ")
        print()
    else:
        word = word.replace("0", "")
        if len(word) % 2 != 0:
            word = word.replace("1", "", 1)
        print(len(word))
        for j in list(word):
            print(j, end=" ")
        print()

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
