def iq_test(numbers):
    arr = []
    z = numbers.split()
    for number in z:
        if int(number) % 2 == 0:
            arr.append("Even")
        else:
            arr.append("Odd")
    if arr.count("Even") > arr.count("Odd"):
        return arr.index("Odd") + 1
    else:
        return arr.index("Even") + 1


z = iq_test("2 4 7 8 10")
print(z)


def queue_time(customers, n):
    z = len(customers)
    arr = []
    time_total = 0
    if z > 0:
        if n >= z:
            return (max(customers))

    else:
        for no in range(n):
            arr.append[no]
            a = max(arr)

    else:
    return (0)



