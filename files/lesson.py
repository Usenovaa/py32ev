'''
Работа с файлами
'''

# open(путь до файла/название файла, 'режим') -> функция, которая позволяет открыть файл и работать с ним


# file = open('/home/hello/Desktop/lesson.py') # - абсолютный путь
# file = open('test.txt') - относительный путь 

'''
Режимы
'''
# 1. r(read) -> режим чтения. Указатель ставится в самое начало. Если файл не существует, ошибка. Режим по умолчанию

# file = open('test.txt', 'r')
# file = open('test.txt')


# 2. w (write) -> Режим записи. Перезаписывает содержимое файла. Если файл не существует, то он его создает

# file = open('index.html', 'w') # создает пустой файл

# 3. a (append) -> режим для дополнения файла (дозапись). Указатель находится в конце. Создаст файл, если такого нет

# file = open('test.txt', 'a')

# 4. x (exclusive) -> Создает уникальные файлы. Режим записи. Если такой файл сущетвует - ошибка

# file = open('test1.txt', 'x')


# 5. t (text) -> текстовый режим 
# rt, wt, at

# 6. b (binary) -> открывает файл в бинарном виде
# rb -> бинарное чтение, wb, ab

# 7. + -> Открывает файл как в режиме записи, так и в режиме чтения
# r+, w+


'''
Методы режима 'r':
1. read(int) -> считывает содержимое файла (определенное кол-во символов), если аргумен не передан, считывает весь файл -> str

2. readline() -> считывает одну строку за раз -> str

3. readlines(int) -> считывает все строки и сохраняет в списке -> list
'''


# file = open('test.txt')
# data = file.readlines() #list
# print(data)
# file.close()


# file = open('test.txt')
# data = file.read(2) #str
# print(data)
# file.close()


# file = open('test.txt')
# data = file.readline() #str
# data2 = file.readline()
# print(data.replace('\n', ''), data2.replace('\n', ''))
# file.close()


# file = open('test.txt')
# data = file.readline() #str test\n
# print(file.tell()) # возаращает индекс где, находится указатель
# file.seek(3) # перемещает указатель на указанный индекс (место)
# data2 = file.readline()
# print(file.tell())
# print(data.replace('\n', ''), data2.replace('\n', ''))
# file.close()


# f = open('test1.txt')
# data = f.read()
# # print(f.tell())
# # f.seek(0)
# data2 = f.readline()
# print(data2)
# f.close()


'''
Методы редима w:
1. write('string') -> записывает с файл переданную строку
2. writelines(list) 
'''
# f = open('test1.txt', 'w')
# f.write('helloworld000000000000000000000000000000')
# f.writelines(['hello ', 'world ', 'py32 ', 'blonds'])
# f.writelines(('test', 'tuple'))
# f.writelines({'one': 1, 'two': 2}) # запишет ключи
# f.writelines([1, 2, 3]) # error
# f.close()

# f = open('test1.txt', 'a')
# # print(f.tell())
# f.write('aaaa')
# f.close()



# try:
#     f = open('test.txt')
#     ...

# finally:
#     f.close()



# with open() ->  контекстный менеджер, открывает файл в указаном режиме и в любом случае закрывает его, без явного вызова метода close()

with open('test1.txt', 'w') as f1:
    f1.write('test\nhello world\nwith open closes automaticlty')

# print(f1.closed)

# file = open('test1.txt')
# file.close()
# print(file.closed)
    

# with open('test1.txt', 'r+') as file:
#     file.write('update')
#     file.seek(0)
#     data = file.read()
#     print(data)
    


# with open('test1.txt', 'w+') as file:
#     file.write('update')
#     file.seek(0)
#     data = file.read()
#     print(data)
    
# with open('test1.txt', 'a+') as file:
#     file.write('update')
#     file.seek(0)
#     data = file.read()
#     print(data)
    

# 'hello' + ' hello'
    


# with open('test1.txt', 'r') as file:
#     data = file.read()
#     # print(data)

# # print(data)
    
# with open('test1.txt', 'w') as file:
#     a = '7777\n' + data
#     file.write(a)
    

# f = open('test1.txt')
# for i in f:
#     print(i)


def test_module_func():
    pass


lesson = 'files'