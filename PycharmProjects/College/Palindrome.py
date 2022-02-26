s = input()
s2 = ''
for i in range(len(s)-1 , -1, -1):
    s2 += s[i]
if s2 == s:
    print(f"{s} is a Palindrome")