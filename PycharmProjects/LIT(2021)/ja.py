import itertools
s = "picoCTF{5}"
ss = '{'
sss = '5}'
arr = ['706c', 'ts_p', 'lien', 'lz_b', 'no_c']
for j in itertools.permutations(arr, 5):
    print(f"picoCTF{ss}{''.join(j)}{sss}")