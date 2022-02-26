for _ in range(int(input())):
    arr = list(input())
    if len(arr) > 10:
        print(f'{arr[0]}{len(arr) - 2}{arr[-1]}')
    else:
        print("".join(arr))