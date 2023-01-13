from random import randint

n=201
Flag=0
while n>0:
    # a=int(input('Игрок 1 введите число конфет от 1 до 28 включительно'))
    a=int(input('Игрок 2 введите число конфет от 1 до 28 включительно'))
    if a>28 or a<1:
        print('Вы ввели некорректное число, введите правильное число')
        continue
    n=n-a
    Flag=1
    if n>0:
        b=randint(1,28)
        print(b)
        n=n-b
        Flag=2
print(f'Победил игрок {Flag}') 

