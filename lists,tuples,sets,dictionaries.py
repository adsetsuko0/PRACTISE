#built-in data collections

#List
l=[1,2,3,4]
#1.Mutable
#2.Indexed
#3.Has duplicates
colors=['blue','green','red','yellow']
fruit = ['blueberry','apple','cherry','banana']
print(colors[1],fruit[1])

#Tuple
t=(1,2,3,4)
#1.Not mutable
#2.Indexed
#3.Has duplicates
record=('John','Python Developer',25)

#Set
s={1,2,3,4}
#1.Mutable
#2.Not indexed
#3.Does not have duplicates


#Dictionaries
d={'a':12,
   'b':13
   }
#1.Mutable
#2.Indexed
#3.Does not have duplicates
ab={'Swaroop':'swaroop@swaroopch.com',
    'Larry':'larry@wall.org',
    'Matsumoto':'matz@ruby-lang.org',
    'Spammer':'spammer@hotmail.com'
    }
print(f'Swaroops adress:{ab["Swaroop"]}')
del ab['Spammer']
print("\nThere's {} contacts in the adress book".format(len(ab)))
for name,address in ab.items():
    print("Contact {0} with {1} address".format(name,address))

ab['Guido']='guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address:",ab['Guido'])