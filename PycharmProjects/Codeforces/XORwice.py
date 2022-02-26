for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    arr1 = list(bin(a))
    arr2 = list(bin(b))
    arr3 = []
    arr1.remove('pre_n_post')
    arr2.remove('pre_n_post')
    arr1.reverse()
    arr2.reverse()
    #print(my_list, arr1000)
    for k, kk in zip(arr1, arr2):
        #print(k, kk)
        if k == '1' and kk == '1':
            arr3.append('1')
        else:
            arr3.append('0')
    arr3.reverse()
    #print(arr3)
    z = int(''.join(arr3), 2)
    print((a ^ z)+(b ^ z))
