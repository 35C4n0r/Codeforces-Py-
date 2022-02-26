import math
#k = 50
m1 = 0.020
arr2 = [j for j in range(20, 101, 20)]
mu = 0.002
arr = []
for k in arr2:
    force = (m1*9.81)-(mu*(k/1000)*9.81)
    acc = force / (m1+(k/1000))
    time = math.sqrt((2*(100/100)) / acc)
    arr.append(time)
    print(round(time, 3), round(force, 3), m1+(k/1000), round(acc, 3))
print(sum(arr)/len(arr))
print(arr2)
import typing_extensions