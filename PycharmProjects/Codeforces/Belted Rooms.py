for _ in range(int(input())):
    n = int(input())
    s = input()
    arr = list(s)
    flag = False
    s = s[-1] + s
    #print(s)
    if ('<' in s) and ('>' in s):
        flag = True
    if not flag:
        print(n)
    else:
        ans = 0
        arr += [arr[0]]
        #print(arr)
        if '-' in arr:
            for j in range(n):
                if arr[j] == '-' or arr[j+1] == '-':
                    ans += 1
            print(ans)

        else:
            print(0)
