marks = 0
count_ACov = 0
count_ACov = 0
count_BCov = 0
count_CCov = 0
count_DCov = 0
count_ECov = 0
count_FCov = 0

for _ in range(12):
    z = None
    try:
        z = input().split("(")
    except EOFError:
        pass
    if count_ACov == 0:
        if "ACov" in z:
            marks += 0.5
            count_ACov += 1
        if 'A)' in z:
            marks += 0.5
    if count_BCov == 0:
        if "BCov" in z:
            marks += 0.5
            count_BCov += 1
        if 'B)' in z:
            marks += 0.5

    if count_CCov == 0:
        if "CCov" in z:
            marks += 0.5
            count_CCov += 1
        if 'C)' in z:
            marks += 0.5

    if count_DCov == 0:
        if "DCov" in z:
            marks += 0.5
            count_DCov += 1
        if 'D)' in z:
            marks += 0.5

    if count_ECov == 0:
        if "ECov" in z:
            marks += 0.5
            count_ECov += 1
        if 'E)' in z:
            marks += 0.5

    if count_FCov == 0:
        if "FCov" in z:
            marks += 0.5
            count_FCov += 1
        if 'F)' in z:
            marks += 0.5

if marks == 1.0:
    marks = 1
if marks == 2.0:
    marks = 2
if marks == 3.0:
    marks = 3
if marks == 4.0:
    marks = 4
if marks == 5.0:
    marks = 5
if marks == 6.0:
    marks = 6
print(str(marks) + " out of 6")


