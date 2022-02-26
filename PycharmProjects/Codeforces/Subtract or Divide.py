def isPrime(n):
    if (n <= 3):
        return False
    # Check from 2 to jkj-1
    for i in range(4, n):
        if (n % i == 0):
            return False
    return True

for _ in range(int(input())):
    n = int(input())
    count = 0
    while n > 1:
        #print('k')
        once = False
        for k in range((n // 2) + 1, 1, -1):
            print(n, k)
            if n%k == 0 and not isPrime(n//k):
                n //= k
                once = True
                count += 1
                break
        if not once:
            n -= 1
            count += 1
    print(count)