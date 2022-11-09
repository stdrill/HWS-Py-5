# Создайте программу для игры в ""Крестики-нолики""

import random

board_size = list(range(1,10))

def board(size):
    print('-'*13)
    for i in range(3):
        print('|', size[0+i*3],'|', size[1+i*3], '|', size[2+i*3], '|')
        print('-'*13)

print(board(board_size))