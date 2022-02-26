for _ in range(int(input())):
    count = 0
    arr = []
    n, c, k = list(map(int, input().split()))
    cake = [0] * n
    for i in range(c):
        ll, ul = list(map(int, input().split()))
        if k == 0:
            if ul == ll:
                cake[ul-1] += 1
                count += 1

            else:
                for m in range(ll, ul+1):
                    cake[m-1] += 1
                    count += 1
        else:
            if ul == ll:
                cake[ul-1] -= 1
                count += 1
                print(count)

            else:
                for m in range(ll, ul+1):
                    cake[m-1] -= 1
                    count += 1
                    print(count)
        print(cake)

    if k == 0:
        if count == (n - cake.count(0)):
            print("Good ")
        else:
            print("Bad")
    else:
        if count == (n - cake.count(0)):
            print("Good")
        else:
            if (n - (cake.count(0) + cake.count(-1))) > cake.count(0):
                print("Bad")
            else:
                print("Good")



