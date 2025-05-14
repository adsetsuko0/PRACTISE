#генерация программой паролей в соответствии с введенными данными

import random
digits='0123456789'
lowercase_letters='abcdefghijklmnopqrstuvwxyz'
uppercase_letters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation='!#$%&*+-=?@^_.'
chars=''

q1=int(input('Сколько паролей должно быть?:'))
q2=int(input('Длина одного пароля:'))
q3= input('Включать ли цифры 0123456789? (y/n):')
q4= input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? (y/n):')
q5= input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? (y/n):')
q6= input('Включать ли символы !#$%&*+-=?@^_? (y/n):')
q7= input('Исключать ли неоднозначные символы il1Lo0O? (y/n):')
if q3.lower()=='y':
    chars+=digits
if q4.lower()=='y':
    chars+=uppercase_letters
if q5.lower()=='y':
    chars+=lowercase_letters
if q6.lower()=='y':
    chars+=punctuation
if q7.lower()=='y':
    for c in 'il1Lo0O':
        chars.replace(c,'')

def generate_password(q2,q1):
    password=''
    for _ in range(q1):
        for _ in range(q2):
            password+=random.choice(chars)
        password+='\n'
    return password
print(generate_password(q2,q1))


