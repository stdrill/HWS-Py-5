# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. 
import random

quant = 2021
# lst = ["Игрок 1", "Игрок 2"]
# rnd = random.randint(0, len(lst) - 1)

# def Game(quant, id):
#     if quant > 0:
#         print(lst[id] + ", введите число: ")
#         playerNum = int(input())
#         if playerNum > 0 and playerNum <= 28 and playerNum <= quant:
#             quant = quant - playerNum
#             if id == 0: id = 1 
#             else: id = 0
#             print(quant)            
#         elif playerNum > quant:
#             print("Введите число от 1 до " + str(quant))
#         else:
#             print("Вы ввели некорректное число! Выберите число от 1 до 28")
#         Game(quant, id)
#     else:
#         print(lst[id - 1] + ", поздравляю с победой!")

# Game(quant, rnd)


lst = ["Игрок", "Бот"]
rnd = random.randint(0, len(lst) - 1)


def vsBot (quant, id):
    if quant > 0:
        print(lst[id] + ", введите число: ")
        if id == 0:
            playerNum = int(input())
            if playerNum > 0 and playerNum <= 28 and playerNum <= quant:
                quant = quant - playerNum
                if id == 0: id = 1 
                else: id = 0
            elif playerNum > quant:
                print("Введите число от 1 до " + str(quant))
            else:
                print("Вы ввели некорректное число! Выберите число от 1 до 28")     
        else:
            if quant > 28:
                botNum = random.randint(1, 28)
                print(botNum)
                quant = quant - botNum
            else:
                botNum = quant
                print(botNum)
                quant = quant - botNum
            if id == 0: id = 1
            else: id = 0
        print(quant)
        vsBot(quant, id)
    else:
        print(lst[id - 1] + ", поздравляю с победой!")

vsBot(quant, rnd)
