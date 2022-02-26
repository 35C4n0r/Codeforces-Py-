for _ in range(int(input())):
    p = input()
    pp = list(p)
    arr = []
    h = input()
    if p in h:
        print("YES")
    elif len(p) > len(h):
        print("NO")
    else:
        for k in pp:
            arr.append(h.find(k))
            h = h.replace(k, "0", 1)
        arr.sort()
        print(arr)
        if -1 in arr:
            print("NO")
        else:
            if arr[0]+len(p)-1 == arr[-1]:
                print("YES")
            else:
                print("NO")

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
