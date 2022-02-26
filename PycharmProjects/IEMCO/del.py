marks = 0
for _ in range(6):
    z = input().split("(")
    if "ACov" in z:
        marks += 0.5
    if 'A)' in z:
        marks += 0.5

    if "BCov" in z:
        marks += 0.5
    if 'B)' in z:
        marks += 0.5

    if "CCov" in z:
        marks += 0.5
    if 'C)' in z:
        marks += 0.5

    if "DCov" in z:
        marks += 0.5
    if 'D)' in z:
        marks += 0.5

    if "ECov" in z:
        marks += 0.5
    if 'E)' in z:
        marks += 0.5

    if "FCov" in z:
        marks += 0.5
    if 'F)' in z:
        marks += 0.5
print(marks)