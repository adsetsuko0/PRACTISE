#задаешь вопрос,а шар дает ответ
import random
answers = ["Бесспорно", "Мне кажется - да", "Пока неясно, попробуй снова", "Даже не думай",
           "Предрешено", "Вероятнее всего", "Спроси позже", "Мой ответ - нет",
           "Никаких сомнений", "Хорошие перспективы", "Лучше не рассказывать", "По моим данным - нет",
           "Можешь быть уверен в этом", "Да", "Сконцентрируйся и спроси опять", "Весьма сомнительно"]

print('Привет, я магический шар, и я знаю ответ на любой твой вопрос!')
name=input('Как мне тебя называть?:')
print(f'Привет, {name}!')
def text(vopros):
    return all(char.isalpha() or char.isspace() for char in vopros)

def choice():
    while True:
        vopros = input('Поделись тем,что тебя интересует:')
        if text(vopros):
            return vopros
        else:
            print('Введи корректный вопрос,пожалуйста.')


def otvety():
    while True:
        n=choice()
        print(random.choice(answers))
        break

otvety()

def cont():
    ans=input('Хотите задать еще один вопрос?(да/нет):\n')
    while True:
        if ans not in ('yes','no','да','нет'):
            ans = input('Вроде, взрослый человек, а на простой вопрос ответить не может...\nПродолжим ("д"/"н")?\n')
        elif ans in ('no','нет'):
            print('Возвращайся, если возникнут вопросы!')
            break
        else:
            return otvety()