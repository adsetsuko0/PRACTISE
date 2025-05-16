import array
a=array.array('d',[1.1,2.1,3.1])
print(a[0])
print(len(a))
a.append(4.1)
print(a)
a.extend([1.2,2.2,3.2])
print(a)
a.insert(4,5.1)
print(a)

from collections import deque
queue=deque()

queue.append(1)
queue.append(2)
queue.append(3)
print(queue)

first=queue.popleft()
print(queue)

#linked list realization
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Создаём узлы
a = Node(1)
b = Node(2)
c = Node(3)

# Связываем их
a.next = b
b.next = c

# Теперь: a → b → c → None

# Вывод всех значений
current = a
while current:
    print(current.value)
    current = current.next


