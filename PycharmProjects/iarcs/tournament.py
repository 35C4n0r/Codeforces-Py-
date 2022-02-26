import itertools
n = int(input())
strength = list(map(int, input().split()))
profit = 0
for e in itertools.permutations(strength, 2):
    profit += abs(e[0]-e[1])
print(profit // 2)

