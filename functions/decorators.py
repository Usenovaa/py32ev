'''
Декораторы
'''
a = print
# print(a)
# a('print')

# def test(func):
#     ...
#     return func

# test1 = test(a)
'''
Функция высшего порядка -> может принимать первым аргументом функция и/или возвращать функцию

функция - объект
'''

# Декоратор -> функция высшего порядка, позволяет обернуть фукцию для расширения ее функционала, без изменения кода


def func():
    print('function')

def test():
    print([i for i in range(1, 11)])
        

def decorator(f):
    print('принимаю функцию ', f.__name__)
    f()

# f = func
# decorator(func)
# # f = test
# decorator(test)
    

def benchmark(func):
    import time
    start = time.time()
    func()
    end = time.time()
    print(f'Время выполнения функции {func.__name__} {end-start}')


def loop():
    i = 0 
    range_number = 1000000
    while i <= range_number:
        print(i)
        i += 1

# benchmark(loop)


def decorator_function(func):
    def wrapper():
        print('Функция обертки')
        print(f'оборачиваем функцию {func.__name__}')
        print('выполняется обернутая функция')
        func()
        print('выход из функции обертки wrapper')
    return wrapper


# wrapper = decorator_function(test)
# wrapper()

# test = decorator_function(test)

@decorator_function
def test():
    print('hello000000000')
# test()

# @ -> синтаксических сахар - позволяет явно указать какой декоратор применяется к функции

# @decorator_function -> используется, чтобы продекарировать функцию. ставится перед определение функции
    

def benchmark(func):
    def wrapper(*args, **kwargs):
        import time
        start = time.time()
        func()
        end = time.time()
        print(f'Время выполнения функции {func.__name__} {end-start}')
    return wrapper


@benchmark
def loop():
    i = 0 
    range_number = 1000000
    while i <= range_number:
        # print(i)
        i += 1

# loop()

@benchmark   
def add():
    i = 0 
    ls = []
    range_number = 1000000
    while i <= range_number:
        ls.append(i)
        # print(i)
        i += 1

# add()
        

def decorator(func):
    def wrapper(arg1):
        print('аргумен, который принимает в себя функция ', arg1)
        func(arg1)
    return wrapper

@decorator
def func1(a):
    print(a)
    print('hellllllllllllloooooooooooooooo')

# func1(6)
    

'''
универсальный -> работает как с функциями , которые принимают аргументы, так и с теми, которые не принимают
'''
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         ...
#         func(*args, **kwargs)
#         ...
#     return wrapper



def smart(func):
    def wrapper(*args, **kwargs):
        if args:
            print('аргументы переданы')
            return 
        func(*args, **kwargs)
        print('test')
    return wrapper

@smart
def division(a, b):
    print(a/b)

# division(4, 7)
    

'''декоратор для вызова функции определенного кол-ва раз'''


def decorator(num):
    def inner_func(func):
        def wrapper():
            for i in range(num):
                func()
        return wrapper 
    return inner_func

@decorator(5)
def test():
    print('hello')

# test()


def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper

def div(func):
    def wrapper():
        return '<div>' + func() + '</div>'
    return wrapper

# ...
#3 @div
#2 @strong
#1 @div
# def get():
#     return 'python 32'

# если ордна функция обернута несколькими декораторами, то они отрабатывают снизу(самый ближний к def) вверх

# print(get())