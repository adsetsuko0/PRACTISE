#перевод числа в двоичную,восьмиричную и шестнадцатиричную системы

num=int(input())

#двоичная
binn=bin(num)
print(binn[2:])

#восьмиричная
octn=oct(num)
print(octn[2:])

#шестнадцатиричная
hexn=hex(num)
print(hexn[2:].upper())

