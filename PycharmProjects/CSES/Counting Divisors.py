def count(num, ans):
    print(num, ans)
    if num % 2 == 0:
        num //= 2
        ans += 2
        count(num, ans)
    else:
        flag = 0
        for k in range(2, num):
            if num % k == 0:
                num //= k
                ans += 2
                flag += 1
                count(num, ans)
        if flag == 0:
            ans += 2
            print(ans)


for _ in range(int(input())):
    i = 1
    z = int(input())
    count(z, 1)
