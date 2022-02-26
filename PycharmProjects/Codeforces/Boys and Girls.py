fin = open('input.txt', 'r')
fout = open('output.txt', 'w')
n, m = list(map(int, fin.readline().strip().split()))
if n > m:
    arr = ["BG"]*m
    arr2 = ["B"]*(n-m)
    stt = ''.join(arr) + ''.join(arr2)
else:
    arr = ["GB"] * n
    arr2 = ["G"] * (m - n)
    stt = ''.join(arr) + ''.join(arr2)
fout.write(f'{stt}')
fout.close()