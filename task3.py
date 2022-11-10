# Создайте программу для игры в ""Крестики-нолики""


board_size = list(range(1,10))

def board_print(size):
    print('-'*13)
    for i in range(3):
        print('|', size[0+i*3],'|', size[1+i*3], '|', size[2+i*3], '|')
        print('-'*13)


def position_choice(player_choice):
    valid = False
    while not valid:
        answer = input("Выберите ячейку для " + player_choice + ":")
        try:
            answer = int(answer)
        except:
            print("Необходимо ввести число")
            continue
        if answer >= 1 and answer <= 9:
            if (str(board_size[answer - 1]) not in "XO"):
                board_size[answer - 1] = player_choice
                valid = True
            else:
                print("Выберите другую клетку")
        else:
            print("Введите число от 1 до 9!")


def win_check(board):
    win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    for each in win_coord:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False


def game(board):
    counter = 0
    win = False
    while not win:
        board_print(board)
        if counter % 2 == 0:
            position_choice("X")
        else:
            position_choice("O")
        counter += 1
        if counter > 4:
            step = win_check(board)
            if step:
                print ("Игрок " + step + " с победой!")
                win = True
                break
        if counter == 9:
            print ("Ничья!")
            break
    board_print(board)

game(board_size)