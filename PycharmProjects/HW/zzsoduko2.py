



board = [[1, 3, 2, 5, 7, 9, 4, 6, 8]
                ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
                ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
                ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
                ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
                ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
                ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
                ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
                ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]


column = []
truth_list = []
final_truth_list = []
for j in range(9):
    for i in range(9):
        column.append(board[i][j])
    for numb in range(1, 10):
        if column.count(numb) == 1:
            truth_list.append('True')
            column[:] = []
print(truth_list)
if truth_list == ['True']*9:
    print('Yay')
else:
    print('No')
