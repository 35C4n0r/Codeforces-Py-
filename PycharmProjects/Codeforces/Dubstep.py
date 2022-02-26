s = input()
#s = s.replace('WUB', '')
s = s.split('WUB')
#s.remove('')
z = s.count('')
for k in range(z):
    s.remove('')
print(' '.join(s))