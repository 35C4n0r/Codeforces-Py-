# 900
def smallestdivisor(n):
    i = 3
    while i ** 2 <= n:
        if n % i == 0:
            return i
        i += 2
    return n


for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    jj = 0
    if n % 2 != 0:
        jj += smallestdivisor(n)
        k -= 1
        n += jj
    n += 2*k
    print(n)

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
