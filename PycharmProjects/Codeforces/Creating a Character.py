t=int(input())
for _ in range(t):
    a,b,c=map(int,input().split())
    print(min(c+1,max(0,(a+c-b+1)//2)))