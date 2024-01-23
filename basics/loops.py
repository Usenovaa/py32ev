'''============ Цикл ==========='''
# Итерация -> это прохождение по последовательности
# Итерируемый объект -> объект по которому можно проходиться, который способен возвращать элементы по одному

# цикл -> это блок кода, который повторяется несколько раз
# используется в тех случаях, когда нужно выполнить определенное действие n-ое количество раз или пройтись по ирерируемому объекту

'''
Синтаксис
'''
# for переменная in итерируемый_объект:
    # код (тело цикла)

# string = 'hello world'
# # string[0] ...

# for i in string:
#     print(i) #выводим в терминал каждый элемент из последовательности

# print(i, 'последний символ') # выполнится позле завершения цикла

# list_ = [1, 2, 3, 4, 5, 6]
# for element in list_:
#     print(element + 9) # к каждому элементу последовательности прибавляем 9

# for i in list_:
#     print(pow(i, 2)) # каждый элемент последовательности возводим в квадрат

# for i in (1, 2, 3, 'hello', 'py'):
#     print(i)

# for i in range(1, 101):
#     print(i)

# ls = []
# for i in range(1, 101):
#     print(i)
#     ls.append(i)
#     # print(ls)

# print(ls)

# for i in 654323456: # числа не итерируемые, нельзя проходиться циклом
#     print(i)
# 'int' object is not iterable

# for i in range(1, 11):
#     if i == 2:
#         print('two')
#     else:
#         print(i)

# for i in range(1, 11):
#     if i % 2:
#         print(i, 'нечетное')
#     else:
#         print(i, 'четное')

# list_ = [1, 2, 3, 4, 5, 6, 7]

# len_ = len(list_)
# print(len_)

# for i in range(len_): # очищение списка используя цикл
#     list_.pop()

# print(list_)

# for i in range(1, 6):
#     print(i, 'i')
#     for j in range(1, 11):
#         print('hello')
#         for b in range(1, 4):
#             print('python')

'''
============== цикл while ===================
'''
# синтаксис
# while условие:
#     тело цикла

# while True: # бесконечный чикл
#     print('hello')


# for i in range(1, 11):
#     print(i)

# counter = 0
# while counter < 10:
#     # counter = counter + 1
#     counter += 1 
#     print(counter)




'''
синтаксический сахар
'''
# num = 10
# num += 1 # инкремент
# num += 3 # num = num + 3
# num -= 1 # дикремент
# num -= 6 # num = num -6
# num *= 2 # num = num * 2
# num /= 5 # num = num / 5
# print(num)


# counter = 0 
# while counter != 10:
#     counter += 1
#     print(counter)

# couter = 10
# while couter != 0:
#     print(couter)
#     couter -= 1
# print('============')

# a = 0
# while a:
#     print('hello')
#  никогда не заработает  bool(0) -> False

# a = input('Введите имя: ')
# while not a:
#     a = input()


'''
=========== Итерация по словарям ===========
'''
dict_ = {'name': 'test', 'password': '12345678', 'email': 'test@gmail.com'}

# for i in dict_: # получаем только ключи
#     print(i)

# for i in dict_: # получение значения по ключу
#     print(dict_[i])
#     print(dict_.get(i))

# print(dict_.keys())
# for key in dict_.keys(): #получение ключей словаря
#     print(key)

# for values in dict_.values(): 
#     print(values)
# получение значений словаря (работает быстрее чем обращение по ключу или вызов метода get)


# for i in dict_.items(): #получение пар (ключ, значение)
#     print(i)
# ('name', 'test')
# ('password', '12345678')
# ('email', 'test@gmail.com')


# a, b = 'an'
# # print(b)
# a, b, c = [1, 2, 3]
# hello, privet= ('hello', 'privet')

# for key, value in dict_.items(): 
#     print(f'Ключ: {key}\nЗначение: {value}')
#распаковываем кортежи с парами на две переменные, где переменная для ключа, а вторая для значения


# 1 -10

# print([i for i in range(1, 11)])


'''бесконечный цикл for'''
# list_ = [1, 2, 3]
# for i in list_:
#     list_.append(i)
#     print(list_)

# sum_ = 0
# num = '7654323456'
# for i in str(num):
#     # print(i)
#     sum_ += int(i)
#     # print(int(i))
# print(sum_)

# num = '7654323456'
# sum_ = 0
# l = 0

# while l < len(num):
#     a = num[l]
#     # print(a)
#     sum_ += int(a)
#     l +=1 
# print(sum_)

'''
============ Ключевые слова в циклах ==========
'''
# break -> полностью выйти из цикла (прерывание цикла)
# continue -> переход к следующей итерации (к следующему прохождению, миную оставшийся код)

# for i in range(1, 11):
#     print(i)
#     break
# '1'

# for i in range(1, 11):
#     print(i)
#     if i == 7:
#         break
# '1' '2' '3' ... '7'

# for i in range(1, 11):
#     if i == 7:
#         break
#     print(i)
# '1' '2' '3' ... '6'


# for  i in range(1, 11):
#     if i == 3:
#         continue
#     print(i)

# for  i in range(1, 11):
#     print(i)
#     if i == 3:
#         continue

# for i in range(1, 11):
#     print(i)
#     continue
#     print(hello)  # никогда не заработает

# i = 0
# while i < 10:
#     if i == 7:
#         break
#     print(i)
#     i += 1 

# i = 0
# while i < 10:
#     i += 1 
#     if i == 7:
#         continue
#     print(i)
   

# i = 0
# while i < 10:
    
#     if i == 7:
#         continue #бесконечный цикл, так как инкремент никогда не сраюотает и i не станет больше 7
#     print(i)
#     i += 1 

'''pass -> ничего не делает. выступает в роли заглушки '''

# for i in 'hello':
#     pass # просто заглушка

# for i in 'hello':
#     ... # просто заглушка

# num = 0
# if num == 0:
#     ... 

'''======== else в циклах ========'''
# else -> проверяет завершился ли цикл "естественным" путям или использовалась инстукция break. Код в else сработает, если не использовался (не сработал) break

# for i in 'hello world':
#     print(i)
#     if i == 'a':
#         break
# else:
#     print('Буквы а в строке нет')

# for i in 'helloaworld':
#     print(i)
#     if i == 'a':
#         break
# else:
#     print('Буквы а в строке нет')

# 14, 23, 26

'''
Задание 14
Создать три числа в списке list_.
Вывести на экран yes, если среди них есть одинаковые, иначе вывести ERROR.
Например, для списка [1, 1, 3], вывод будет:

yes 
а для списка [1, 2, 3]:

ERROR 
# '''
# list_ = [1, 1, 3]

# if len(list_) == len(set(list_)):
#     print('ERROR')
# else:
#     print('yes')

'''Задание 23
Вам дан список, напишите код, который будет соединять в новый список элементы по n-ному шагу
Например:

step = 3
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']'''

step = 3
list_ = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# new_list = []

# for i in range(step):
#     inner = []
#     for b in range(i, len(list_), step):
#         inner.append(list_[b])
#     new_list.append(inner)
# print(new_list)
    # print(inner)


'''Задание 26
Вам даны 2 списка, напишите код, который будет выводить разницу первого списка от второго и наоборот
Например:

colors1 = ["red", "orange", "green", "blue", "white"]
colors2 = ["black", "yellow", "green", "blue"]
У Вас должен быть всего один print
'''

colors1 = ["red", "orange", "green", "blue", "white"]
colors2 = ["black", "yellow", "green", "blue"]

l1 = []
l2 = []
for i in colors1:
    if not i in colors2:
        l1.append(i)

for i in colors2:
    if not i in colors1:
        l2.append(i)
print(l1, l2)




