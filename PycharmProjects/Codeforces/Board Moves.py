for _ in range(int(input())):
    n = int(input())
    n = ((n-3)//2)+1
    ans = ((4*n)*(n+1)*((2*n)+1)) // 3
    print(ans)