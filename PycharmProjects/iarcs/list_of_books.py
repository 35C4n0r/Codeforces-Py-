a = int(input())
list_book = list(map(int, input().split()))
b = []
n = int(input())
for _ in range(n):
    b.append(int(input()))
for index in b:
    print(list_book[index - 1])
    list_book.remove(list_book[index - 1])


