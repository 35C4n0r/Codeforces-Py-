'''def dfs(xxx):
    global sna
    global link
    for kk in lis[xxx]:
        xxx = kk
        if kk in lis:
            link += 1
            dfs(xxx)
        else:
            sna = max(sna, link)
            link = 1


link = 2
lis = {}
sna = 0
for _ in range(int(input())):
    s = input()
    s = s.replace('reposted', '')
    arr, pre_n_post = s.split()
    arr = arr.lower()
    pre_n_post = pre_n_post.lower()
    #print(arr, pre_n_post)
    if pre_n_post in lis:
        lis[pre_n_post] .append(arr)
    else:
        lis[pre_n_post] = [arr]
#print(lis)
dfs('polycarp')
print(sna)'''
d = {'polycarp': 1}
for i in range(int(input())):
    j, k, l = input().lower().split()
    d[j] = d[l] + 1
    #print(d)
print(max(d.values()))
