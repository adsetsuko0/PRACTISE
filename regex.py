import re
import sys

text= 'короче тут буду искать фразы'
match=re.findall('буду',text)
print(match)

text = "My SSN is 123-45-6789"
match = re.search(r"\d{3}-\d{2}-\d{4}", text)

if match:
    print("Найдено:", match.group())

print(re.findall(r"\d", "house 221b,num 7"))
print(re.findall(r"\w","user00_59"))
print(re.findall(r"[abc]", "apple, banana, cherry"))
print(re.findall(r"[^xyz]",'osi z i y'))
print(re.findall(r"[a-z]", 'Hello 123!'))
print(re.findall(r'[A-Za-z0-9]','User_007!'))
print(re.findall(r"[a\-z]", "a-z dash"))
print(re.findall(r'\bJava\B', 'Java and JavaScript'))
print(re.findall(r"a.b", "acb a_b a-b a\nb"))
print(re.findall(r'a.+b','a298b atkfb a----b'))
print(re.findall(r'^Hello','Hello world'))
print(re.findall(r'world$','hello world'))
print(re.findall(r'a*','aaaa aaa aab'))
print(re.findall(r'ab*','aaabbb abb ab a'))
print(re.findall(r'ab+', 'ab aaabb abbb'))
print(re.findall(r'.+at','rat bat brat'))
print(re.findall(r'ab?','ab abb aa a bb b')) #ab? означает:
# символ "a", за которым идёт 0 или 1 "b".
print(re.findall(r'apple|orenge', 'str rasp apple grapes'))

text = "User: john42, ID: 789"
match = re.search(r"User: (\w+)", text)
print(match)

s = "Обладаешь ли ты налогооблагаемой благодатью?"
res = re.split(r' ', s, maxsplit=1)
print(res)
st = re.compile('угнал')
res1 = st.findall("Карл у Клары угнал Maclaren, а Клара у Карла угнала Corvette.")
res2 = st.findall("Карл у Клары угнал кораллы, а Клара у Карла угнала кларнет.")
print(res1, res2, sep='\n')
print(re.findall(r"\Bро", 'розовая от мороза'))
print(re.findall(r'ин\B','синий апельсин'))

stroka='an example string:kot'
match=re.search(r'string:\w+', stroka)
if match:
    print(f'found:', match.group())
else:
    print('not found')

match=re.search(r'@\d+\s+\d+\s+\d', '@123  00   1')
print(match.group())

adress='pm on my email address ajfjkdss-@someshi.com'
match=re.search(r'([\w.-]+)@([\w.-]+)', adress)
print(match.group())
if match:
    print('local part:',match.group(1))