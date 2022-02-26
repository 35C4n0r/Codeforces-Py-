doit = (int(input()))
# THIS CODE IS PROPERTY OF NO_SOUL
for _ in range(int(doit)):
    n, x = list(map(int, input().split()))
    my_list = list(map(int, input().split()))
    arr100 = list(map(int, input().split()))
    my_list.sort()
    flag = False
    arr100.sort(reverse=True)
    for k in range(n):
        if my_list[k] + arr100[k] > x:
            print("No")
            flag = True
            break
    if not flag:
        print("Yes")
    if _ != doit - 1:
        input()