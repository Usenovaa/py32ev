'''
Встроенные функции
'''

# print
# len
# input
# dict
# list
# set
# tuple
# dir
# int
# str
# complex
# range
# sorted
# hex
# oct
# ...


'''
lambda -> анонимная функция (таже самая функция, только без имени)
'''

# def <name>():
#     body

def name(): return False
# print(name())

'''
Синтаксис
'''
# lambda параметры: результат

def add(a, b): return a + b
# print(add(5, 66))

'''
хоть она и анонимная, мы можем к ней обратиться(вызвать) через переменную
'''
result = lambda a, b: a + b
# print(result(88, 98))

result = lambda a, b, c: (a, b, c)
# print(result(88, 98, 6))

# keys = lambda dict1: dict1.keys()
# print(keys({'one': [], 'two': {}}))

last = lambda list_: list_[-1]
# print(last([8, 4, 6, 2]))
# print(last(['d', 0, False]))
# print(last((1, 2, 3, 54)))
# print(last('hello'))

[1, 2, 3, 4]
''
()
{}
{}
'''
map(func, iterable) -> функция высшего порядка, принимает первым аргументом функцию, вторым итерируемый объект. Применяет func для каждого элемента iterable
'''
# result = map(int, ['1', '2', '3'])
# print(result) # map object

# print(type(list(result)[1]))

# print(list(result))

# result = list(map(int, ['1', '2', '3']))
# print(result)

# def sq(num):
#     return num ** 2

# result = list(map(sq, [4, 6, 8]))
# print(result)

# result = list(map(lambda x: x > 0, [-44, 99, 0, 5, -7]))
# print(result)

# в функцию map передать анонимную функцию, которая увеличивает число на 1

# result = list(map(lambda x: x + 1, [-44, 99, 0, 5, -7]))

'''
map на цикле for
'''
# import time

# start = time.time()
# func = lambda x: x + 1
# res = []
# for i in [4, 5, 2, 6, 77]:
#     res.append(func(i))
# print(res)
# end = time.time()
# t1 = end - start
# print(format(float(t1), 'f'), 'for')

# start = time.time()
# result = list(map(lambda x: x + 1, [-44, 99, 0, 5, -7]))
# print(result)
# end = time.time()
# t2 = end - start
# print(format(float(t2), 'f'), 'map')
# print(f'{end-start:.5f}')



'''
filter(func, iterable) -> результат, последовательность элементов, которые прошли фильтрацию 
'''

# def filter_num(number):
#     if number % 2:
#         return True
    
# result = list(filter(filter_num, [1, 2, 3, 4, 5, 6, 7]))
# print(result)


# def filter_str(string):
#     if string[-1] == 'e':
#         return True

# result = list(filter(filter_str, ['hello', 'test', 'file', 'code', 'love']))

# print(result)

# result = list(
#     filter(
#         lambda x: x[-1] == 'o', ['hello', 'open']
#     )
# )
# print(result)





def startswith_vowel(string: str):
    vowels = 'АЕОИЮЯЭЁУЫ'
    # print(tuple(vowels))
    return string.startswith(tuple(vowels))

# l = lambda string: string.startswith(tuple('АЕОИЮЯЭЁУЫ'))

# result = list(
#     filter(
#         startswith_vowel, 
#         ['Айдын', 'Айхан', 'Султан', 'Эртай', 'алиса']
#     )
# )

# print(result)


'''
filter через цикл for
'''

# ls = []

# for i in ['Айдын', 'Айхан', 'Султан', 'Эртай', 'алиса']:
#     if startswith_vowel(i):
#         ls.append(i)

# print(ls)


'''
reduce(func, iterable) -> нужно импортировать из модуля functools
возвращает один результат (ипользуется для нахождения суммы, мин и макс числа ...)
'''
# sum()
# min()    заменили reduce
# max()

from functools import reduce

ls = [0, 77, 5, 3, 44]
res = reduce(lambda x, y: x + y, ls)
# print(res)
# print(sum(ls))

ls = [77, 5, 3, 44]
res = reduce(lambda x, y: x * y, ls)
# print(res)

'''
reduce  на цикле for
'''
ls = [77, 5, 3, 44]
def mul(a, b):
    return a * b

res = ls[0]
for i in ls[1:]:
    res = mul(res, i)

# print(res)



'''
enumerate(iterable, [start-> число, по умолчанию 0] ) -> возвращает генератор состоящий из tuple (число, элемент из iterable) -> нумерует элементы
'''
# list_ = ['a', 'b', 'c', 'd']
# for i in enumerate(list_):
#     print(i)


# list_ = ['a', 'b', 'c', 'd']
# for index, elemet in enumerate(list_):
#     print('index - ', index, ' element - ', elemet)

# print(enumerate(ls)) # enumerate object

# res = list(enumerate(ls))
# print(res)

# res = list(enumerate(ls, 6))
# print(res)


'''
zip(iterable, iterable -> *iterable ) -> соединяет последовательности 
'''
ls = [1, 2, 3, 4]
ls2 = [9, 8, 7, 5, 6]

# print(zip(ls, ls2)) #zip object

# print(list(zip(ls, ls2))) 
l1 = list(zip('hello', {'one': 1, 'two': 2}, [6, 7, 8, 9, 0]))
# print(l1) #ориентируется на самый короткий


'''
all() -> возвращает bool, True, если все элементы соответстуют условию
'''

# ls = [1, 2, 3, 4]
# print(all(ls)) # True


ls = [1, 2, 3, 4, 0]
# print(all(ls)) #False

# ls = [1, 2, 3, 4, '0']
# print(all(ls)) #True

# ls = [1, 2, 3, 4, False, 0, '']
# print(all(ls)) #False

# ls = [2, 3, 4]

# print(all(item >= 2 for item in ls ))

'''
any() -> True, если хотябы один элемент True
'''
ls = ['', 0, False, ' ']
# print(any(ls)) #True

ls = [0, '', False]
# print(any(ls)) #False

ls = [2, 3, 4]

# print(any(item == 4 for item in ls)) #True
