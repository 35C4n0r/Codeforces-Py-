ALPHAs = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ARRs = list(ALPHAs)
s = input()
arr2 = list(s)
cg = 0
cl = 0
for k in s:
    if k in ARRs:
        cg += 1
    else:
        cl += 1
if cl >= cg:
    print(s.lower())
else:
    print(s.upper())