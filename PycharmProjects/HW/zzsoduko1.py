def done_or_not(board):
    print(board)
    column = []
    truth_list = []
    final_truth_list = []
    for row in board:
        for number in range(1, 10):
            if row.count(number) != 1:
                return'Try again!'
            else:
                final_truth_list.append('True')
    if final_truth_list == ['True']*81:
        for j in range(9):
            for i in range(9):
                column.append(board[i][j])
            for numb in range(1, 10):
                if column.count(numb) == 1:
                    truth_list.append('True')

            column[:] = []

        if truth_list == ['True'] * 81:
            return('Finished!')
        else:
            return('Try again!')
