'''
Тип данных Списки list(). Функция range(). Цикл for. Кортеж tuple()
'''

# списки - изменяемые, упорядоченные, индексируемые

# литералы -> [] (константа, выражение, которое создает объект) используя "" -> создаем str, используя [] -> создаем list 

'''======= Создание списков ========'''

# 1. list_ = [] # пустой список
# 2. list_1 = list('hello') # ['h', 'e', 'l', 'l', 'o']
# print(list_1)

# list(iterable) -> создает список 

#3. list_2 = list(range(11))
# print(list_2)

# range(start, end, step) -> возвращает последовательность элементов, если передать только end, последовательность чисел начнется с 0 и закончится до end (end не включительно)

list_ = [1, 2, 3, 4, 'hello', True, None, ['a', 'b']]
list_[0] # 1
list_[4] # hello
# print(list_[4][2]) # l
# print(list_[-2]) # None
# print(list_[-1]) #['a', 'b']
# print(list_[-1][1]) # b

# list_[0] = 9 # изменили элемент списка под индексом 0
# print(list_)

# a = 'hello'
# a[0] = 'l'

# print(dir(list))

'''
================ Методы списков ===============
'''
# .append(element) -> добавляет элемент в конец списка
# list_ = [1, 2, 3]
# # print(id(list_))
# list_.extend(567890)
# list_.append('hello') 
# list_.append([4, 5, 6])
# print(list_) #[1, 2, 3, 'hello']
# print(id(list_))

# .extend(iterable) -> расширяет список добавляя в конец каждый элемент iterable по отдельности
# list_ = ['makers', True, None, 1.2, 99, 6]
# list_.extend('hello')
# list_.extend([1, 2, 3])
# list_.extend(567890) # ошибка
# print(list_)
# 4567890

# .insert(index, element) -> добавляет element по указанному index
# list_ = [3, 6, 9]
# list_.insert(0, 'hello')
# list_[100] # ошибка
# list_.insert(100, 'world') # добавит в конец
# print(list_)

# .index(element, [start], [end]) -> возвращает индеч elemeta
list_ = [
    'hello', 'makers', True,
    None, True, False, [4, 5, 6]
    ]
# print(list_.index(True)) #2
# print(list_.index(True, 3, 6)) #4 (поиск начнется с 3 индекса и закончится на 6 индексе)
# list_.index('test') # будет ошибка (так как такго элемента нет в списке)

# print(list_[-1].index(4)) #0

# .clear() -> очищаеть список
list_ = [
    'hello', 'makers', True,
    None, True, False, [4, 5, 6]
    ]
# list_.clear()
# print(list_) # []

# .count(element) -> считывает кол-во повторений elementа в списке
list_ = [
    'hello', 'makers', True,
    None, True, False,'python', 'python', 'python', [4, 5, 6]
    ]

# print(list_.count(True)) # 2
# print(list_.count('python')) # 3
# print(list_.count('py')) # 0

# len() -> возвращает кол-во элементов (объектов) в списке
# print(len(list_)) #10 


# .pop([index]) -> удаляет элемент из списка по индексу, если индекс не передать -> удаляет полседний элемент списка, также возвращает удаленный элемент

list_ = [
    'hello', 'makers', True,
    None, True, False,'python', 'python', 'python', [4, 5, 6]
    ]

# popped = list_.pop() # [4, 5, 6]
# # print(list_, '===========', popped)
# popped2 = list_.pop(0)  #'hello'
# popped2 = list_.pop(110) # ошибка
# print(list_) 

# .remove(element) -> удаляет первый принятый элемент из списка
list_ = [
    'hello', 'makers', True,
    None, True, False,'python', 'python', 'python', [4, 5, 6]
    ]
# list_.remove('python')
# list_.remove('test') # ошибка
# print(list_)


# .reverse() -> изменяет список, переворачивая его
# list_ = [1, 2, 3, 4, 5, 6]
# list_.reverse()
# print(list_)

# .sort([reverse=True]) -> сортирует список, состоящий из элементов одного типа
# list_ = [77, 5, 43, 6, 9, 'hello'] # ошибка
# list_ = [77, 54, 66, 3, 0, 9]
# list_.sort() # по возрастанию
# list_.sort(reverse=True) # по убыванию
# print(list_)

# list_ = ['hello', 'apple', 'makers', 'ab', 'a']
# list_.sort()
# print(list_)

# .copy() -> поверхносно копирует список
# list_ = ['hello', 'apple', 'makers', 'ab', 'a']
# new_list = list_.copy()
# new_list.append('py32')
# print(new_list)
# print(list_)

# print(dir(list))

'''============ Кортеж tuple ============'''
# литералы -> , ()
# tuple() -> создает кортеж

# неизменяемый, индексируемый, упорядоченный, итерируемый

# a = (1, 2)
# print(a[0])

# .count(element) -> считывает кол-во повторений elementа в кортеже
list_ = (
    'hello', 'makers', True,
    None, True, False,'python', 'python', 'python', [4, 5, 6]
)
# print(list_.count(True)) # 2
# print(list_.count('python')) # 3
# print(list_.count('py')) # 0

# .index(elenemt, [start], [end]) -> работает также как и в списке


# tuple_ = () # пустой кортеж
# tuple_ = (3,) # кортеж с одним элементом
# tuple_ = tuple('hello')
# tuple_ = 1, 2, 3 # кортеж
# tuple_ = 1,  # кортеж с одним элементом
# print(tuple_)
# print(type(tuple_))


''' =========== Цикл =========== '''
# цикл -> это блок кода, который повторяется какое-то кол-во раз


# 
# list_ = [1, 2, 3, 4, 5]
# list_.pop()
# list_.pop()

# for переменная in list_:
    # тело1


# for i in list_:
#     print('работаем')
#     print(i)

# print(list_)


# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_[0])
# print(list_[1])
# print(list_[2])
# print(list_[3])
# print(list_[4])
# print(list_[5])
# # ...


# for i in list_:
#     print(i)

# print('hello')
# print('hello')
# print('hello')
# print('hello')
# print('hello')

# for i in range(10):
#     print(f'Привет {i}')

# list_ = []

# str_ = input('введите: ')

# for i in str_:
#     list_.append(i)

#     print(list_)