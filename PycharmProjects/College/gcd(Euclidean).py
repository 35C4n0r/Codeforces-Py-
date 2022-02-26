def euclid(a, b):
    if a == 0:
        return b
    return euclid(b % a, a)


aa = int(input())
bb = int(input())
print(euclid(aa, bb))
