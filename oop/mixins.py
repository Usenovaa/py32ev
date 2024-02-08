'''
Миксины
'''

# классы примеси, используются только для наследования

'''
Работа с Миксинами
1. Принято давать названия, заканчивающиеся на Mixin: CreateMixin, MoveMixin...
2. Миксины не предназначены для создания от них объектов
3. Нужны для расширения функционала (возможностей) класса 
'''

# class Object:
#     def stop():
#         ...

#     def move():
#         ...

#     def sleep():
#         ...


# class Person(Object):
#     pass

# class Car(Object):
#     pass


class StopMixin:
    def stop(self):
        print('стою')

class MoveMixin:
    def move(self):
        print('двигаюсь')

class SleepMixin:
    def sleep(self):
        print('сплю')


class Person(SleepMixin, StopMixin, MoveMixin):
    pass

class Car(StopMixin, MoveMixin):
    pass

# person = Person()
# person.sleep()
# person.stop()
# person.move()

# car = Car()
# car.move()
# car.stop()
# car.sleep()


class CreateMixin:
    def create(self, key, todo):
        if key in self.todos:
            return 'задача под таким ключем уже существует'
        self.todos[key] = todo
        
class DeleteMixin:
    def delete(self, key):
        deleted = self.todos.pop(key, '')
        return deleted
    
class UpdateMixin:
    def update(self, key, new_todo):
        if key not in self.todos:
            return 'Задачи с таким ключем нет'
        self.todos[key] = new_todo

class ReadMixin:
    def read(self):
        return self.todos


class Notes(CreateMixin, DeleteMixin, UpdateMixin, ReadMixin):
    todos = {}

# todo = Notes()
# CRUD
# todo.create('tasks', '20 tasks for list')
# # # todo.create('tasks', '88 tasks for list')
# # todo.delete('tasks')
# # print(todo.todos)
# todo.create('task2', 'do hw')
# todo.create('task3', 'bla bla bla')
# print(todo.read())
# todo.update('tasks', 'hello')
# print(todo.read())
    

class FlyMixin:
    def fly(self):
        print('я могу летать')

class WalkMixin:
    def walk(self):
        print('Я могу ходить')

class SwimMixin:
    def swim(self):
        print('я могу плавать')
  

class Human(WalkMixin, SwimMixin):
    pass

class Fish(FlyMixin, SwimMixin):
    pass

class Duck(FlyMixin, SwimMixin, WalkMixin):
    pass


# objects = [Human(), Fish(), Duck(), Human()]

# for i in objects:
#     i.swim()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class P(Person):
    def __init__(self, name, age, f):
        super().__init__(name, age)
        self.faculty = f

a = P()