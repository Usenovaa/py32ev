'''
=========== Comprehensions ============
генерация последовательности в одну строку с использованием цикла (синтаксический сахар x += 1) 
'''

# list, dict, set есть три вида


# Синтаксис
# 1. результат for элемент in итерируемый объект
# 2. результат for элемент in итерируемый_объект if фильтр

'''
============ list comprehension =============
'''
# упрощенный подход к созданию списков с использованием цикла  for, а также if-else 

# list_ = []

# for i in range(1, 11):
#     list_.append(i)

# print(list_)
    
# list_1 = list((i for i in range(1, 11)))
# print(list_1)

# list_2 = [i for i in range(1, 11)]
# print(list_2)

# list_3 = [i**2 for i in range(1, 11)]
# list_3 = [i*i for i in range(1, 11)]
# list_3 = [pow(i, 2) for i in range(1, 11)]

# ['hello', 'hello', 'hello']

# list_ = []
# for i in range(10):
#     list_.append('hello')

# ['hello'for i in range(10)]


# list_ = [i for i in range(1, 21) if i%2 == 0]
# list_ = [i for i in range(0, 21, 2)]
# print(list_)

# ls = [input() for i in range(10)]
# print(ls)

# ls = ['четное' if i%2 == 0 else 'нечетное' for i in range(1, 11)]
# print(ls)

# ls = [1, 5, 3, 2, 'hello', 8, 10, 2.8, 2.0, 'a', 'b', [1, 2, 3], {'a': 2}]
# ls1 = ['четное' if i%2 == 0 else 'нечетное' for i in ls if type(i) == int or type(i) == float]
# print(ls1)

'''
если в comprehension используем if-else -> указываются в самом начале (результат)
если только if -> в конце
'''

'''
================== Set comprehension ================
'''
# почти тоже самое что list comprehension, только элементы не дублируются и не сохраняется порядок, используются {}

# ls = [1, 2, 5, 6, 99]
# set_ = {i for i in ls}
# print(set_)

# set_ = set()
# for i in ls:
#     set_.add(i)


'''=========== dict comprehension ============'''
# {k: v}

# {1: 1, 2: 2}

# dict_ = {i: i for i in range(1, 11)}
# print(dict_)


# dict_ = {i: i**2 for i in range(1, 11)}
# print(dict_)

# list_ = [1, 1, 2, 2, 2, 2, 3, 3, 4]
# {1: 2, 2: 4, ...}

# dict_ = {i: list_.count(i) for i in list_}
# print(dict_)

# d = {'a': 2, 'b': 77}
# {'a': 'четное', 'b': 'нечетное'}

# dict_ = {k: v for k, v in d.items()} #получаем такой же словарь

# dict_ = {k: 'четное' if v%2 == 0 else 'нечетное' for k, v in d.items()}
# print(dict_)

# for k, v in d.items():

# 'даны 2 списка, создайте словарь, где ключи - элементы 1 списка, а значения - второго'
list1 = [1,2,3,4,5]
list2 = ['a','b','c','d','e']

# {1: a, 2: b, 3: c}

# print(list(range(len(list1))))
# dict_ = {list1[index]: list2[index] for index in range(len(list1))}
# print(dict_)

# d = {'a': 2, 'b': 77}
# dict_ = {v: k for k, v in d.items()}
# print(dict_)


'''
============= вложенные comprehensions =============
'''

# dict_ = {0: [0], 1: [0, 1], 2: [0, 1, 2] }

# [x for x in range(1, 11)]

# dict_  = {i: [x for x in range(i+1)] for i in range(11)}
# print(dict_)

emp = {
    'id_1' : {
        'last_name': 'hello',
        'age': 23
    },
    'id_2' : {
        'last_name': 'test',
        'age': 88
    }
}

# 1. dict_ = {k: v for k, v in emp.items()}
# print(dict_)

# 2. dict_ = {k: {k1: v1  for k1, v1 in v.items()} for k, v in emp.items()}
# print(dict_)


# 3. dict_ = {k: {k1.upper(): float(v1) if k1 == 'age' else v1  for k1, v1 in v.items()} for k, v in emp.items()}
# print(dict_)