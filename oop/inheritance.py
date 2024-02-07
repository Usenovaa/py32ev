'''
Основные принципы ООП: Наследование
'''
# основные: Наследование, Полиморфизм и Инкапсуляция
# Абстракция, Ассциация(Агрегация, Композиция)


'''
Наследование - принцип ООП, в котором мы можем унаследовать, переопределить и использоватть в дочернем классе все методы и атрибуты родительского класса
'''

'''
Синтаксис
'''
class РодительскийКласс:
    ...
    # методы_и_атрибуты_Родительского_класса

class ДочернийКласс(РодительскийКласс):
    ...
    # методы_и_атрибуты_Дочернего_класса

# class Animal:
#     def make_sound(self):
#         print('I am animal')

# class Croco(Animal): #Унаследовали все у родителького класса Animal
#     pass

# croco = Croco()
# croco.make_sound()
    

# class A(): class A: class A(object):


class A:
    def method(self):
        print('Метод класса А')

class B(A):
    '''
    Наследовали все методы и атрибуты класса А
    '''
    def method_b(self):
        print('Метод класса B')


# b = B()
# b.method()
# b.method_b()

# a = A()
# a.method()
# a.method_b() # родительским классам не доступный дочение методы и атрибуры


class C(A):
    '''
    Наследовали все методы и атрибуты класса А
    и полностью переопределили родительский метод method
    '''
    def method(self):
        print('Метод класса С')

# c = C()
# c.method()
'''
mro (method resolution order) -> порядок поиска методов и атрибутов
'''
# print(C.mro())
# print(C.__mro__)

'''
======== Виды наследования ========
'''
# одиночное наследование (когда у дочернего класса только один родитель (родительский класс))
# иерархическое наследование (когда у одного родителя несколько дочерних классов)
# многоуровневое наследование (когда мы наследуемся от класса у которого уже есть родитель)
# множественное наследование (когда дочерний класс наследуется от нескольких родительских)
# гибридное наследование (когда используется несколько видов наследования)


class Person:
    def __init__(self, name, age, last_name):
        self.name = name 
        self.age = age
        self.last_name = last_name

    def display_info(self):
        print(f'Name: {self.name}')


class Employee(Person):
    def work(self):
        print(f'{self.last_name} {self.name} works')


class Studen(Person):
    # def __init__(self, name, age, last_name, class_):
    #     self.name = name 
    #     self.age = age
    #     self.last_name = last_name
    #     self.class_ = class_

    # def __init__(self, name, age, last_name, class_):
    #     '''
    #     дополняем родительский метод
    #     '''
    #     Person.__init__(self, name, age, last_name)
    #     self.class_ = class_

    def __init__(self, name, age, last_name, class_):
        '''
        super() -> используется для обращения к родительскому классу
        чтобы избежать обращения по имени (имя может измениться)
        '''
        super().__init__(name, age, last_name)
        self.class_ = class_

    def study(self):
        print(f'{self.name} studies')


# sam = Studen('Sam', 21, 'Parker', 'IT')
# Studen.study(sam)
# # sam.display_info()
# sam.study()
        

'''
Создайте класс А и в нем определите метод my_range с помощью которого будут создаваться списки изменяемого диапазона
'''
# class A:
        
#     def my_range(self, start, end):
#        l = list(range(start, end + 1))
#        print(l)

# a = A()
# a.my_range(1,22)


# isinstance() -> проверяет является ли объект экземпляром класса
# issubclass() -> проверяет, является ли класс дочерним


# e = Employee('', 1, '')
# print(isinstance(e, Employee))
# print(isinstance(e, Person))
# print(isinstance(e, object))
# print(isinstance(e, Studen))

# print(issubclass(Employee, Person))
# print(issubclass(Studen, Person))
# print(issubclass(Person, Employee))

'''Создайте класс MyString, который будет наследоваться от str. Определите 2 своих метода:
- append, который будет принимать строку и добавлять её в конец исходной
- pop, который удаляет из строки последний элемент и возвращает его.'''


# class MySring(str):
#     pass

# a = MySring()
# a.upper()

class MySring(str):
    def __init__(self, str_):
        self.str_ = str_
    def append(self,str1):
        self.str_ += str1

    def pop_(self):
        a = self.str_[-1]
        self.str_ = self.str_[:-1]
        return a 

    def __str__(self):
        return self.str_
    
# a = MySring('test')
# # print(a)
# a.append('hello')
# # print(a)
# print(a.pop_())
# print(a)


'''
========= Множественное наследование =========
'''

class Lion:
    color = 'black'

class Lioness:
    color = 'brown'

class Child(Lion, Lioness):
    pass

# child = Child()
# print(child.color)


'''
==== Проблемы множественного наследования ====
'''

# 1. Проблема ромба
# решена при помощи mro 
# проблема: два раза заходил в один и тот же класс

class A:
    pass

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

#       A

#    B     c

#       D

# print(D.__mro__)

class X:
    ...

class Y:
    ...

class Z:
    ...

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):
    pass

# M B A X Y Z obj

# print(M.__mro__)

'''
========= проблема скрещенного наследования (перекрустного) НЕ РЕШЕНА ==========
'''

# class A:
#     pass

# class B:
#     pass

# class C(A, B):
#     pass

# class D(B, A):
#     pass

# class M(C, D):
#     pass

