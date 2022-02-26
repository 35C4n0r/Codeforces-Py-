# 900
n = int(input())
hl = input()
contest = 0
for _ in range(n):
    flight = input()
    x = flight.find(hl, 0, 3)
    if x == 0:
        contest -= 1
    else:
        contest += 1
if contest == 0:
    print("home")
else:
    print("contest")

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
