import random


for i in range(3):
    print(random.random())

for j in range(3):
    print(random.randint(10, 20))

members = ["congress ", "BJP"]
print(random.choice(members))