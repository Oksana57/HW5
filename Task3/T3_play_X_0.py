import T3_print_board
board=list(range(1,10))

def play_X_0(play_char):
    flag=False
    while not flag:
        player_answer=input('В какую клетку поставим ' + play_char + '? ')
        try:
            player_answer=int(player_answer)
        except:
            print('Просили же выбрать номер клетки. Попробуй еще')
            continue
        if player_answer>=1 and player_answer<=9:
            if (str(board[player_answer-1]) not in 'X0'):
                board[player_answer-1]=play_char
                flag=True
            else:
                print('Клетка занята')
        else:
            print('Вы ввели некорректное число. Введите число от 1 до 9')


