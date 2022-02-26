# 900
for _ in range(int(input())):
    p = input()
    p_copy = p
    pp = list(p)
    arr = []
    h = input()
    hh = list(h)
    if p in h:
        print("YES")
    elif len(p) > len(h):
        print("NO")
    elif len(p) == len(h):
        for k in pp:
            arr.append(h.find(k))
            h = h.replace(k, "0", 1)
        arr.sort()
        if -1 in arr:
            print("NO")
        else:
            print("YES")
    else:
        for k in hh:
            if len(arr) == len(pp):
                break
            elif k in pp:
                arr.append(h.find(k))
                h = h.replace(k, "0", 1)
                p = p.replace(k, "@", 1)
                print(p) #####
                print(h) #####
                print(arr)
                pp = list(p)
            else:
                arr = []
                p = p_copy
                pp = list(p_copy)
        arr.sort()

        if -1 in arr:
            print("NO")
        else:
            if min(arr)+len(p)-1 == max(arr):
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
