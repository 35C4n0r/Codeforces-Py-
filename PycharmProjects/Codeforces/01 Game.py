'''for _ in range(int(input())):
    k = input()
    count = 0
    lis = list(map(str, list(k)))
    if set(lis) == {"0"} or set(lis) == {"1"}:
        print("NET")


    while len(lis) != 0 and set(lis) != {"0"} and set(lis) != {"1"}:
        k = k.replace("01", "")
        lis = list(k)
        count += 1

    if count % 2 == 0 and count != 0:
        print("NET")
    elif count % 2 != 0:
        print("DA")'''

for _ in range(int(input())):
    s = input()
    print('DA' if min(s.count('0'), s.count('1')) % 2 == 1 else 'NET')


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
