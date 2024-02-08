'''
Основные принципы ООП: Инкапсуляция
'''

# 1. Объединение всех свойств и методов в одну капсулу (класс)
# 2. Ограничение доступа к методам и атрибутам, т.е для сокрытия данных


# как связь
class Phone:
    number = '+996777565656'

    def print_number(self):
        print(self.number)

# a = Phone()
# a.number
# a.print_number()
        
# Связываем поведение объекта с его данными
        
'''
инкапсуляция - как сокрытие данных
'''

class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

# pt = Point(4, 7)
# pt.x = 'hello'
        

'''
3 модификатора доступа
1. public - публичный (без нижних подчеркиваний вначале) - данные доступны всем -> x, y, number, name ...

2. _protected -> защищенный (c одним нижним подчеркиванием) данные доступны внутри класса и в дочерних классах -> _x, _y, _number ...

3. __private -> приватный (с двумя нижними подчеркиваниями) -> слжат только для обращения внутри класса -> __x, __y, __number
'''
        

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

# pt = Point(8, 9)
# # pt._y = 'hello'
# print(pt._y)
'''
реализовано на уровне договоренности не обращаться вне класса
'''

class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def test(self):
        self.__y += 33
        print(self.__y)
        

pt = Point(0, 77)

# pt.test()
# print(pt._Point__y)
# print(pt.__x, pt.__y) # AttributeError
# print(pt.__dict__)

'''
более защищенный, все атрибуты сохраняются под другим именем, которое формируется
из _НазваниеКласса__названиеАтрибута

можно обратиться через эти имена и менять значения атрибутов, но так делать не рекомендуется
'''

# для работы с приватными и защищенными атрибутами объявляются методы getter (получение значения) и setter (задать новое значение)


class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
    
    def set_coord(self, new_x, new_y):
        '''
        setter/getter -> можно реализовать дополнительную логику проверки
        '''
        if type(new_x) in (int, float) and type(new_y) in (int, float):
            self.__x = new_x
            self.__y = new_y
        else:
            raise ValueError(
                'Координаты должны быть числами'
            )

    def get_coords(self):
        return self.__x, self.__y

# pt = Point(5, 7)
# # pt.set_coord(6, 'hello') Error
# pt.set_coord(6, 88) 
# print(pt.get_coords())
    


class Solution:
    __private_attr = 210

    def __private_method(self):
        '''
        приватные методы, так же используются только в классе
        '''
        print('приватный метод')

    def method(self):
        print(self.__private_attr)
        self.__private_method()

# a = Solution()
# a.method()
# a._Solution__private_method()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, new_age):
        if type(new_age) == int and new_age in range(1, 101):
            self.__age = new_age
        else:
            print('Invalid age')

# a = Person('Sam', 55)
# # a.set_age('hello')
# # a.set_age(-99)
# a.set_age(44)
# print(a.get_age())
            

# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.__age = age

#     @property
#     def get_age(self):
#         '''
#         декоратор property позволяет обращаться к методу как к атрибуту (без вызова)
#         '''
#         return self.__age
    
#     @get_age.setter
#     def set_age(self, new_age):
#         if type(new_age) == int and new_age in range(1, 101):
#             self.__age = new_age
#         else:
#             print('Invalid age')


# a = Person('test', 77)
# a.set_age = 78
# print(a.get_age)


class Person:
    def __init__(self, name, age):
        self.name = name 
        self.__age = age

    @property
    def age(self):
        '''
        декоратор property позволяет обращаться к методу как к атрибуту (без вызова)
        '''
        return self.__age
        
    @age.setter
    def age(self, new_age):
        if type(new_age) == int and new_age in range(1, 101):
            self.__age = new_age
        else:
            print('Invalid age')


# a = Person('test', 77)
# a.age = 78
# print(a.age)
            

class Car:
    def __init__(self, owner, color, year):
        self.__owner = owner
        self.color = color
        self.year = year

    '''
    определите getter и setter для работы с приватным атрибутом __owner (ИСПОЛЬЗОВАТЬ ДЕКОРАТОРЫ)
    '''
    @property
    def owner(self):
        return self.__owner
    
    @owner.setter
    def owner(self, new_owner):
        if type(new_owner) == str:
            self.__owner  = new_owner
        else:
            print('qwertyui')

lada = Car('Ильгиз', 'белая', 2023)
lada.owner = 'Аббас'
print(lada.owner)
