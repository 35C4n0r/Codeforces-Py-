width, h_max = list(map(int, input().split()))
height = list(map(int, input().split()))
position = 0
holding = False
for instruction in list(map(int, input().split())):
    if instruction == 0:
        break
    elif instruction == 1:
        if position > 0:
            position -= 1
    elif instruction == 2:
        if position < width - 1:
            position += 1
    elif instruction == 3:
        if not holding and height[position] > 0:
            height[position] -= 1
            holding = True
    elif instruction == 4:
        if holding and height[position] < h_max:
            height[position] += 1
            holding = False
for i in height:
    print(i, end=' ')




