for _ in range(int(input())):
    n, l = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    arr2 = arr.copy()
    time = 0
    timea = []
    time2 = 0
    timeb = []
    speed = 1
    speed2 = 0
    dist2 = l
    dist = 0
    arr2.reverse()
    answer = 0
    met = False
    z = l / 2
    # for (smh, smh2) in zip(lis, arr1000):
    #for (smh, smh2) in zip(range(0, jkj+1), range(jkj, -1, -1)):
    while True:
        for aa, bb in zip(range(len(arr)), range(len(arr))):
            dist += arr[aa] - arr[aa-1]
            time += (arr[aa] - arr[aa-1]) / speed
            timea.append(time)
            speed += 1
            dist2 -= abs(arr2[bb] - arr2[bb-1])
            cob = bb
            coa = aa
            time2 += (abs(arr2[bb] - arr2[bb-1])) / speed
            timeb.append(time2)
            speed2 += 1
            print(dist, dist2, timea, timeb)
            if dist >= dist2:
                answer = timea[-2] + abs(arr[aa] - arr[bb]) // (speed2+speed)
                break
        if answer > 0:
            break
        break
    print(answer)
