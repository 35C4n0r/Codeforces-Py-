"""
ID: jay20ma1
LANG: PYTHON3
TASK: ride
"""

alphabet_arr_raw = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alpha_arr = list(alphabet_arr_raw)
fin = open('ride.in', 'r')
fout = open('ride.out', 'w')
name1 = fin.readline().strip("\n")
name2 = fin.readline().strip("\n")
z = 1
z2 = 1
for k in name1:
    z *= alpha_arr.index(k) + 1
z %= 47
for l in name2:
    z2 *= alpha_arr.index(l) + 1
z2 %= 47
if z2 == z:
    fout.write("GO" + '\n')
else:
    fout.write("STAY" + '\n')
fout.close()
