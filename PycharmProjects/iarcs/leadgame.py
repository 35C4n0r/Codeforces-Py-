pla1 = []
pla2 = []
final_list1 = []
final_list2 = []
player = None
n = int(input())
for _ in range(n):
    z = list(map(int, input().split()))
    count1 = z[0]
    pla1.append(z[0])
    pla2.append(z[1])
for i in range(n):
    if pla1[i] > pla2[i]:
        final_list1.append(pla1[i] - pla2[i])
        result1 = max(final_list1)
    else:
        final_list2.append(pla2[i] - pla1[i])
        result2 = max(final_list2)
if result1 > result2:
    player = 1
    print(player, result1)
else:
    player = 2
    print(player, result2)






try:
    pla1 = []
    pla2 = []
    final_list1 = []
    final_list2 = []
    n = int(input())
    for _ in range(n):
        z = list(map(int, input().split()))
        pla1.append(z[0])
        pla2.append(z[1])
    for i in range(n):
        if pla1[i] > pla2[i]:
            final_list1.append(pla1[i] - pla2[i])
            result1 = max(final_list1)
        else:
            final_list2.append(pla2[i] - pla1[i])
            result2 = max(final_list2)
    if result1 > result2:
        print("1 " + str(result1))
    else:
        print("2 " + str(result2))


except EOFError as e:
    pass









