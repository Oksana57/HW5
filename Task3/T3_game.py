board=list(range(1,10))
import T3_print_board
import T3_play_X_0
import T3_win_cod
T3_print_board.print_board(board)

def game(board):
    count=0
    win=False
    while not win:
        # T3_print_board.print_board(board)
        if count%2==0:
            T3_play_X_0.play_X_0('X')
        else:
            T3_play_X_0.play_X_0('0')
        count+=1
        if count>4:
            temp=T3_win_cod.victory(board)
            if temp:
                print('Ура победа')
                win = True
                break
        if count==9:
            print('Ничья')
            break
    
    # print(T3_print_board.print_board(board))  

game(board)              