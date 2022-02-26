# cook your dish here
nam = []
for _ in range(int(input())):
    name = ' '
    name=input().lower()
    if name.count("berhampore") >= 1 and name.count("serampore") >= 1:
        nam.append("Both")
    elif name.count("berhampore") >= 1:
        nam.append("GCETTB")
    elif name.count("serampore") >= 1:
        nam.append("GECTTS")
    else:
        nam.append("Others")
for j in nam:
    print(j)

