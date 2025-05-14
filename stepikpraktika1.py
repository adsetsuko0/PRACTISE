import random
num=random.randint(1,100)
print('Добро пожаловать в числовую угадайку!')
print('У вас есть 8 попыток,чтобы угадать число.Начинаем!')
def is_valid(vvod):
    if vvod.isdigit():
        if 1<=int(vvod)<=100:
            return True
        else:
            return False
    return False

def isvalid():
    while True:
        n=input('Введите число:')
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')


def compare():
    popytki=0
    while True:
        n=isvalid()
        if n<num:
            print('Ваше число меньше загаданного.')
            popytki+=1
            print(f'Осталось {8-popytki} попыток.')
            if popytki==8:
                print('Не осталось попыток')
                break
        elif n>num:
            print('Ваше число больше загаданного.')
            popytki+=1
            print(f'Осталось {8 - popytki} попыток.')
            if popytki==8:
                print('Не осталось попыток')
                break
        else:
            print('Вы угадали!')
            break

compare()

def continue_game():
    ans = input('Хотите продолжить ("д"/"н")?\n')
    while True:
        if ans not in ('y', 'д', 'n', 'н'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('n', 'н'):
            print('До новых встреч!!!')
            return False
        else:
            return compare()
continue_game()
