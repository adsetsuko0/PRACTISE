#функция chr()

print('Вас приветствует программа по шифровке/дешифровке текста шифром Цезаря!')
k=int(input('Введите значение шага для шифровки(>0) либо дешифровки(<0):'))
enalpha=[chr(i) for i in range(65,91)] + [chr(j) for j in range(97,123)]
rualpha=[chr(i) for i in range(1040,1104)]
def shifr(text):
    if txt[0] in enalpha:
        alphabet=enalpha;kolvo=26
    else:
        alphabet=rualpha;kolvo=32
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].isupper():
                print(alphabet[(alphabet.index(text[i])+k)%kolvo],end='')
            else:
                print(alphabet[(alphabet.index(text[i]) + k) % kolvo + kolvo], end='')
        else:
            print(text[i],end='')

txt=input('Введите текст:')
shifr(txt)
print()
#без функции,с переменной

print('ШИФР ЦЕЗАРЯ')
print('Добро пожаловать в программу,посвященную такому методу шифрования как Шифр Цезаря.')
lang=input('Для начала,пожалуйста,выберите язык вашей фразы.Введите ru/eng:')
direction=input('Что бы вы хотели сделать:шифрование/дешифрование:')
if direction=='Ш':
    question=input('Вы знаете шаг сдвига?Введите yes/no:')
    if question=='yes':
        szag=input('Введите шаг сдвига:')
else:
    szag = input('Введите шаг сдвига:')
origtext=input('Введите вашу фразу:')

ru_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'  # 32 буквы (0-31)
en_alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 26 букв (0-25)
symbols = ('1234567890 .,?"!\'-')

def cipher(text,alphabet,szag):
    res=[]
    for letter in text:
        szagi=alphabet.find(letter.lower())+int(szag) #сдвиг буквы
        if letter in symbols:
            res.append(letter)
            continue
        elif szagi<len(alphabet):
            if szagi<0:
                if lang=='en':
                    szagi+=26
                elif lang=='ru':
                    szagi+=32
            if letter==letter.upper():
                ch_lett=alphabet[szagi]
                res.append(ch_lett.upper())
            else:
                ch_lett=alphabet[szagi]
                res.append(ch_lett)
        elif szagi>=len(alphabet):
            if letter==letter.upper():
                ch_letter=alphabet[szagi-len(alphabet)]
                res.append((ch_letter.upper()))
            else:
                ch_letter=alphabet[szagi-len(alphabet)]
                res.append(ch_letter)
    res=''.join(res)
    return res

def isvalid(direction,lang):
    if direction=='шифрование' or direction=='дешифрование':
        if lang=='ru' or lang=='en':
            return True
    else:
        return False

if isvalid(direction,lang):
    if direction=='шифрование':
        if lang=='en':
            print(cipher(origtext,en_alphabet,szag))
        else:
            print(cipher(origtext,ru_alphabet,szag))
    elif direction=='дешифрование':
        if lang=='en':
            if question=='yes':
                print(cipher(origtext,en_alphabet,-(int(szag))))
            else:
                for i in range(len(en_alphabet)):
                    print('Вариант',i,cipher(origtext,en_alphabet,i))
        elif lang=='ru':
            if question == 'yes':
                print(cipher(origtext, ru_alphabet, -(int(szag))))
            else:
                for i in range(len(ru_alphabet)):
                    print('Вариант', i, cipher(origtext, ru_alphabet, i))
else:
    print('Вы ошиблись в вводе, повторите попытку')


