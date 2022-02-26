for _ in range(int(input())):
    n = int(input())
    arr=list(map(int,input().split()))
    arr=sorted(arr)
    while len(arr) > 0:
        print(arr.pop(len(arr)//2),end=" ")
    print()


