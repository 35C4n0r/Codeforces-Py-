lst=list(map(int,input().split()))
n,lst=lst[0],lst[1:]
lst1=set(lst)
ans=1
if n!=1:
    ans=2
for i in range(n):
    for j in range(i+1,n):
        a=max(lst[i],lst[j])
        b=abs(lst[i]-lst[j])
        c=2
        while True:
            d=a+b
            if d in lst1:
                a=d
                c+=1
            else:
                break
        ans=max(ans, c)
print(ans)