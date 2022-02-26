board =[[1, 3, 2, 5, 7, 9, 4, 6, 8]
        ,[4, 9, 8, 2, 6, 1, 3, 7, 5]
        ,[7, 5, 6, 3, 8, 4, 2, 1, 9]
        ,[6, 4, 3, 1, 5, 8, 7, 9, 2]
        ,[5, 2, 1, 7, 9, 3, 8, 4, 6]
        ,[9, 8, 7, 4, 2, 6, 5, 3, 1]
        ,[2, 1, 4, 9, 3, 5, 6, 8, 7]
        ,[3, 6, 5, 8, 1, 7, 9, 2, 4]
        ,[8, 7, 9, 6, 4, 2, 1, 5, 3]]
row = []
column = []
truth_list2 = []
truth_list1 = []
for i in range(9):
    for j in range(9):
        row.append(board[i][j])
        for number in range(1, 10):
            if row.count(number) == 1:
                truth_list1.append('True')
                row[:] = []
print(truth_list1)
if truth_list1 == ['True'] * 9:
    for j in range(9):
        for i in range(9):
            column.append(board[i][ j])
            for number in range(1, 10):
                if column.count(number) == 1:
                    truth_list2.append('True')
                    column[:] = []
    if truth_list2 == ['true'] * 9:
        print ('Finished')
    else:
        print ('Try again!')
else:
    print('Wrong')