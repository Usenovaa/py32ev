'''
строки str()
'''
# неизменяемый тип данных, предназначен для хранения текста (последовательности символов), всегла заключается в кавычки

string1 = 'строка с одинарными кавычками,""" внутри нельзя использовать одинарные кавычки'
string2 = "строка с двойными кавычками,'''' внутри нельзя использовать двойные кавычки"
# string3 = "неправильная строка' # ошибка
string4 = '''
здесь можно использовать любые кавычки и
переносить текст на следующую строку
'''
string5 = """
здесь можно использовать любые кавычки и
переносить текст на следующую строку          
"""


# len() -> возвращает кол-во символов в строке (длину строки)

# print(len(string5)) # пробелы тоже считаются за символы

# hello = 9
# hello
# 'hello'


'''
========== Экранированные последовательности ==========
'''
# это последовательность начинающаяся с символа "\" 

'''
экранизация строк
'''
'\n' # перенос строки
'\t' # табуляция
'\'' # отображение '
"\"" # отображение "
'\\' # отображение \
'\r' # возвращает каретку в начало строки
'\v' # перенос строки на новую линию со смещением вправо на длину предудущей строки
'\a' # гудок встроенного в систему динамика (не работает)

# print('hello \nworld')
# print('hello  \tworld')
# print('\'hello world\'')
# print("\"hello world\"")
# print('hello world \\')
# print('hellooooooooooo \rworld')
# print('hello000000000000\vworld')


# + -> объединение строк (конкатенация строк, склеивание строк)

# a = 'hello'
# b = 'world'
# print(a + ' ' + b) # hello world

# * -> дублирование строк
# print('hello' * 3)

'''========== Индекс =========='''
# порядковый номер элементов в строке

# 'hello world'
# 012345678910
#    ... -2-1
# str_ = 'hello world'
# print(str_[0])
# print(str_[5])
# print(str_[10])

# str_2 = 'gjvbkldsjn sjdvldk;fkljbkhjvv;lkjklbkhvjkblknljbkhhkbln;lk'
# print(str_2[-1])

'''========== срез ========'''
# нахождение подстроки в строке 

str_ = 'Makers bootcamp'
# print(str_[0:6]) # до 6го элемента 
# print(str_[:6]) # часть строки 'Makers' 
# print(str_[:]) # вся строка
# print(str_[7:11])
# print(str_[7:])
# print(str_[4:9])
# print(str_[1])
# print(str_[8])
# print(str_[-2])

# [start:end:step]
# print(str_[::2])
# print(str_[::3])
# print(str_[::4])

# print(str_[::-1]) # перевернули строку
# print(str_[::-2])

# срез -> нахождение подстроки [start: stop: step], начиная от start, заканчивая до end (end не включительно) (step по умолчанию 1(записывается каждый элемент строки))
# [1:] -> начинаем с элемента под первым индексом и до конца
# [:4] -> начинаем с 0го индекса и до 4 (4 не включительно)
# [4:7] -> начинаем с 4го индекса и до 7 (7 не включительно)
# [::], [:], [0::1] -> получаем всю строку
 

'''========= Методы ========='''
# str.lstrip
# str.split

# .lstrip() -> удаляет пробелы в левой части строки (вначале)
# a = '                         hello'
# print(a)
# print(a.lstrip())


# .rstrip() -> удаляет пробелы в конце строки (справа)
# a = ' hello    '
# print(len(a))
# print(len(a.rstrip()))


# .strip() -> убирает пробелы вначале и в конце строки


# # .split(разделитель) ->  разделяет строку по разделителю и возвращает тип данных списки, если разделитель не указать будет делить по пробелу
# a = 'hello, world, makers, bootcamp..'
# b = a.split() #['hello,', 'world,', 'makers,', 'bootcamp..']
# c = a.split(',') #  ['hello', ' world', ' makers', ' bootcamp..']
# d = a.split('o') 
# # print(d)

# a = 'banana...,,,asd'
# print(a.rstrip('.,asd'))


# print(dir('h'))

'''Методы на is -> проверяют и возвращают True/False'''
# .isdigit() -> состоит ли строка только из чисел
# .isalpha() -> состоит ли строка только из букв
# .isalnum() -> состоит ли строка только из букв и чисел
# .islower() -> состоит ли строка из символов в нижнем регистре
# .isupper() -> состоит ли строка из символов в верхнем регистре
# .isspace() -> состоит ли строка из неотображаемых символов (пробел, экранированные последовательности '\n', '\t', ...)
# .istitle() -> Начинается ли каждое слово в строке с верхнего регистра (все остальные символы должны быть в нижнем регистре)

# str_ = 'helLo'
# print(str_.islower()) #False
# str_2 = '34567865'
# print(str_2.isdigit()) #True
# ...


# .lower() -> переводит символы в нижний регистр (возвращает новую строку в нижнем регистре)
str_1 = 'HELLO Hello heLLo'
# new_str = str_1.lower()
# print(str_1, ' -> ', new_str)

# .upper() ->  переводит символы в верхний регистр
str_2 = 'Makers bootcamp'
# new_str = str_2.upper() # MAKERS BOOTCAMP
# print(new_str)

# .swapcase() -> переводит в противоположный регистр
str_3 = 'Py 32 Makers BOOTcamp'
# print(str_3.swapcase())

# .title() -> переводит первую букву каждого слова в верхний регистр, а все остальные в нижний
str_4 = 'привет рЕБЯТА'
# new_str = str_4.title() #Привет Ребята
# print(new_str)

# .capitalize() -> переводит первый символ каждой строки в верхний регистр
str_5 = 'hello World. привет'
# new_str = str_5.capitalize()
# print(new_str)

# .replace(old, new, [count]) -> заменяет old на new, если указать count, то только указанное кол-во раз
# str_6 = 'ha ha ha ha ha'
# new_str = str_6.replace('ha', 'new', 4)
# print(new_str)


# .find(value, [start], [end]) -> возвращает индек value (если value нет в строке вернет -1)
# str_7 = 'hello world'
# print(str_7.find('l')) 
# print(str_7.find('u')) #-1

# .index(substring, [start], [end]) -> возвращает индекс substring
# str_7 = 'hello world'
# print(str_7.index('l')) 
# print(str_7.index('u')) #ошибка

# .startswith(substring, [start], [end]) -> проверяет, начинается ли строка с substring
# str_8 = 'hello world!'
# print(str_8.startswith('h')) #True
# print(str_8.startswith('hello')) #True
# print(str_8.startswith('world')) #False
# print(str_8.startswith('world', 6)) #True

# .endswith(substring, [start], [end]) -> проверяет, заканчивается ли строка с substring
# str_8 = 'hello world!'
# print(str_8.endswith('!')) #True
# print(str_8.endswith('world')) #False
# print(str_8.endswith('world!')) #True


# .count(substring) ->  считает кол-во вхождений substring в строке
# str_8 = 'hello world hello world hello!'
# print(str_8.count('hello'))
# print(str_8.count('l'))

# .zfill(width) -> делает длинну строки равной width, по необходимости недостающие символы заполняет нулями
# str_9 = 'hello'
# print(str_9.zfill(10)) #00000hello
# print(str_9.zfill(3)) #hello


# 'разделитель'.join(interable/список) ->  объеденяет элементы iterable в строку используя разделитель
list_ = ['hello', 'world', 'python', 'py32']
print(list_)
# print('-->'.join(list_)) #hello-->world-->python-->py32


'''======= Форматирование строк динамические строки  ======='''
# inp = input('Введите имя: ')
# a = 'Привет, inp'
# print(a)

# %
# inp = input('Введите имя: ')
# a = 'Привет, %s' %inp
# print(a)

# .format()
# inp1 = input('Введите имя: ')
# inp2 = input('Введите фамилию: ')
# a = 'Прив{}ет,  {}'.format(inp1, inp2)
# print(a)

# f-строка -> итерполяция строк
# inp1 = input('Введите имя: ')
# inp2 = input('Введите фамилию: ')
# a = f'Привет, {inp1} {inp2}'
# print(a)
