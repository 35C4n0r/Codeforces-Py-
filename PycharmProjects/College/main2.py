n = input()
dig = "1234567890"
alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
arr = list(dig)
arr2 = list(alpha)
arr3 = list(n)
flag = False
count = 0
for _ in arr3:
    if _ in arr:
        flag = True
        count += 1
if flag:
    print(f"There is/are {count} digit(s) in the given input")
else:
    print("There are no digits in the given input")

