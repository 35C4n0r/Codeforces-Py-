primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151]
mmm = 1073741824
a, b, c = list(map(int, input().split()))
arr = []
count = 0


def d(x):
    ans = 1
    for i in primes:
        if x < i:
            break
        power = 0
        while x % i == 0 and x >= i:
            x = x//i
            power += 1
        ans *= (power+1)
    return ans


for smh1 in range(1, a + 1):
    for smh2 in range(1, b + 1):
        for smh3 in range(1, c + 1):
            xxx = d(smh1 * smh2 * smh3)
            count += xxx
print((count % mmm) % mmm)