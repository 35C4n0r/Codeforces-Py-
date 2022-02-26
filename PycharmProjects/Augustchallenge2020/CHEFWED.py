for _ in range(int(input())):
    n, k = list(map(int, input().split()))
    f_word = list(map(int, input().split()))
    count = 0
    for j in f_word:
        if f_word.count(j) > 1:
            count += 1
    if k == 1:
        print(count)