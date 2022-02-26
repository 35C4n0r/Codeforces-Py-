def find_even_index(arr):
    z = len(arr)
    if sum(arr[1: z + 1]) == 0:
        return (0)
    else:
        for j in range(1, z + 1):
            if sum(arr[0:j]) == sum(arr[j + 1:z + 1]):
                return (j)



