n = str(input(""))
if int(n) % 2 != 0:
    print("Weird")
else:
    if int(n) in range(21, 101):
        print("Not Weird")
    if int(n) in range(6, 21):
        print("Weird")
    if int(n) in range(2, 5):
        print("Not Weird")





