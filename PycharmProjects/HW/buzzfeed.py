for fizzbuzz in range(51):
    if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")

    elif fizzbuzz % 3 == 0:
        print("fizz")

    elif fizzbuzz % 5 == 0:
        print("buzz")
    else:
         print(fizzbuzz)
