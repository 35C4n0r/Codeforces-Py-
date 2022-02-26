number = [1, 2, 3, 4, 5, 6, 4, 7, 2, 3, 2, 1 ]
unique = []
for new in number:
    if new not in unique:
        unique.append(new)
print(unique)

# or


print(set(number))












