'''
=========== Обработка исключений =============
'''

# Ошибки -> проблема с синтаксисом (исправляем самостоятельно)
# 1. SyntaxError -> забыли двоеточие, скобку
# 5g = 0
# 2. IndentationError -> неправильные отступы
# 3. TabError -> неправильная табуляция (при смешивании tabов и пробелов)


# Исключения: (код написан правильно, но программа не работает или работает не так)
# 1. ZeroDivisionError 
#       ArithmeticError
# 2. NameError
# 3. IndexError
# 4. KeyError
# 5. ImportError
# 6. ValueError
# 7. TypeError 
# 8. AttributeError
# 9. BaseException (прородитель всех ошибок)


ZeroDivisionError # вызывается при делении на 0
# 3 % 0
# 3 // 0  #- ZeroDivisionError: integer division 
# 3 / 0   #        or modulo by zero


NameError # вызывается при обращении к несуществующей переменной
# hello  - NameError: name 'hello' is not defined.
# suum()
# random


IndexError # вызывается при  обращении к несуществующему индексу
# ls = [1, 2, 3]
# ls[9] - IndexError: list index out of range
# ls.pop(9)


KeyError # вызывается при обращении по несуществующему ключу
# dict_ = {'a': 1}
# dict_['b'] - KeyError: 'b'
# dict_.pop('c') - KeyError: 'c'


ImportError # неправильный импорт
# from  math import pi2 - ImportError: cannot import name 'pi2' from 'math' (unknown location)
# import mathh - ModuleNotFoundError: No module named 'mathh'


ValueError #при неправильной распаковке, припереводи в другой тип данных (если объект не может быть переведен)
# a, b = '1' - ValueError: not enough values to unpack (expected 2, got 1)
# int('23j') - ValueError: invalid literal for int() with base 10: '23j'


TypeError # связано с типами данных, при вызове методов передаем меньше или больше аргументов

# for i in 542353224:        TypeError: 'int' object is 
#     ...                             not iterable
# 5 + '5' - TypeError: unsupported operand type(s) for +: 'int' and 'str'
# [].append() - TypeError: list.append() takes exactly one argument (0 given)
# [].append(1, 2) - TypeError: list.append() takes exactly one argument (2 given)
# {[]: 1} - TypeError: unhashable type: 'list'
# input('1', '2') - TypeError: input expected at most 1 argument, got 2

AttributeError # при обращении к несуществующему методу (атрибуту)
# [].replace('old', 'new') - AttributeError: 'list' object has no attribute 'replace'

# 'dffdf'.append('hello') - AttributeError: 'str' object has no attribute 'append'

'''исключение'''
# print('==================')
# print(name) # верхний print отработает, код сломается на 76 строке

'''ошибка'''
# print('========================')
#     print('error') # код сломается сразу



'''
========== Обработка исключений (try ... except) =======
'''
# try:
#     код, который может вызвать исключение

# except (Исключение, которое может возникнуть):
#     код, который сработает, если в try возникло исключение

# else:
#   код, который отработает, если в try не возникло исключение

# finally:
#   код, который сработает в любом случае

# try:
#     number = int(input('  '))
# except ValueError:
#     print('Нужно вводить числа')
#     # number = int(input('  '))

# print('ничего не сломалось')

# try:
#     print(number)
# except NameError:
#     print('значение не присвоено')

# try:
#     print(number)
# except:
#     print('значение не присвоено')

'''
обрапотка нескольких исключений
'''

# a = 9
# b = 0

# try:
#     print(с / b)

# except (ZeroDivisionError, NameError):
#     print('на ноль делить нельзя!!!!!!!!!')

# a = 9
# b = 0
# try:
#     print(с / b)

# except ZeroDivisionError:
#     print('на ноль делить нельзя!!!!!!!!!')
# except NameError:
#     print('переменная не объявлена')

# try:
#     while True:
#         print('hello')
# except KeyboardInterrupt:
#     print('ctrl + c')


'''
else в try ... except
'''
# dict_ = {'a': 5, 'b': 10, 'c': 15}

# try:
#     key_ = input()
#     res = dict_[key_]
#     print(res)
# except KeyError:
#     print('Такого ключа нет')
# else:
#     print(res, 'Блок else')
    # работает только, если исключение не возникло в блоке try


'''
finally в try ... except
'''
# a = 9
# try:
#     print(a + 88)
# except NameError:
#     print('Обработали NameError')
# finally:
#     print('блок finally')

# try:
#     a + b

# except Exception as e: # Exception используется для обработки всех исключений
#     print(e, '===========') # e -> описание исключения
#     print(e.__class__) # исключение

# from random import randrange as rdrg


'''
raise -> Исскуственно вызывает исключение
'''
# age = int(input('Введите возраст '))
# if age < 18:
#     raise ValueError('Доступ закрыт')
# print(age)

# age = int(input('Введите возраст '))
# if age < 18:
#     raise  так нельзя!
# print(age)