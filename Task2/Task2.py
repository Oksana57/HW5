# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента? ()
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

n = 201
Flag = 0
while n > 0:

    while True:
        a = int(input('Игрок 1 введите число конфет от 1 до 28 включительно'))
        if a > 28 or a < 1:
            print('Вы ввели некорректное число, введите правильное число')
        else:
            n = n-a
            Flag = 1
            break

    if n > 0:
        while True:
            b = int(input('Игрок 2 введите число конфет от 1 до 28 включительно'))
            if b > 28 or b < 1:
                print('Вы ввели некорректное число, введите правильное число')
                continue
            else:
                n = n-b
            Flag = 2
            break

print(f'Победил игрок {Flag}')

# Нужно 1 игорку взять остаток от деления 2021 на 28 это 27 конфет, а потом брать конфет
#  29-(количество конфет взятых 2 игроком)