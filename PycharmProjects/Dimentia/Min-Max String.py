for _ in range(int(input())):
    arr = []
    d = int(input())
    for i in range(d):
        j = input()
        arr.append(j)
    q = int(input())
    w = q.copy()
    lol = []
    z = 0
    for k in range(q):
        command = input()
        if len(command) == 5:
            x = int(command[2])
            c = command[4]
            arr.insert(len(arr) + 1, f"{arr[x - 1]}{c}")
        elif command == 2:
            for h in range(d):
                if







