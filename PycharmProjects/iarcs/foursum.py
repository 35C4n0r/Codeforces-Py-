arr = list(map(int, input().split()))
n = arr[0]
t = arr[1]
s = arr[2:]
count = 0
import itertools
for i in itertools.combinations(s, 4):
   if sum(i) == t:
     count += 1
print(count)
