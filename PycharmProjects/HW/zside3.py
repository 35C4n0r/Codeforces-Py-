def dirReduc(arr):
    arr2 = []
    final_arr = []
    meaning = {
        "NORTH": 1,
        "SOUTH": -1,
        "EAST": 2,
        "WEST": -2
    }
    for direction in arr:
        arr2.append(meaning.get(direction))
        z = sum(arr2)

        meaning2 = {
            1: "NORTH",
            -1: "SOUTH",
            2: "EAST",
            -2: "WEST"
        }



z = dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])
print((z))



