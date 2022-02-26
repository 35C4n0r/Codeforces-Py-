n = int(input())
friends = {}
for i in range(n):
    a, b = map(int, input().split())
    if a in friends:
        friends[a].append(b)
    else:
        friends[a] = [b]
    if b in friends:
        friends[b].append(a)
    else:
        friends[b] = [a]
'''print(network)
for k in network:
    print(network[k], k)'''
co = False
for each in friends:
    if len(friends[each]) != 2:
        co = True
if co or len(friends) < 5:
    print("WIN")
else:
    print("FAIL")
