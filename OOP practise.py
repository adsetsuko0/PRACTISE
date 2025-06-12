#guess the number codewars
import random
print('Добро пожаловать в числовую угадайку!Вам потребуется угадать число от'
      '1 до 100')
print('У вас есть 8 попыток,чтобы угадать число.Начинаем!')
random_num=random.randint(1,100)


def is_digit(vvedi_num):
    if not vvedi_num.isdigit():
        raise TypeError('Нужно ввести ЧИСЛО')
    return True


def vvod_num():
    while True:
        num=input('Введите ваше число:')
        if not is_digit(num):
            raise TypeError('')
