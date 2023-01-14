board=list(range(1,10))

def victory(board):
    win_cod=((0,1,2), (0,3,6),(1,4,7), (2,5,8),(3,4,5), (6,7,8),(0,4,8),(2,4,6))
    for each in win_cod:
        if board[[each[0]]==board[each[1]]==board[each[2]]]:
            return board[each[0]]
    return False        