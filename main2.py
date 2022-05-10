class Animal():
    def __init__(self, x, y):
        self.name = x
        self.gender = y
        self.energy = 100

    def report_information(self):
        print(self.name)
        print(self.gender)
        print(self.energy)

    def dance_with_someone(self, someone):
        print(self.name, 'dances with', someone.name)
        self.energy -= 10
        someone.energy -= 10

class Person(Animal):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.species = 'human'

    def say_something(self):
        print('Ah')

    def __str__(self):
        return "Hi, my name is %s." % self.name

class Dog(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.species = 'dog'

    def say_something(self):
        print('Woof')

class Cat(Animal):
    def __init__(self, name, gender):
        super().__init__(name, gender)
        self.species = 'cat'

    def say_something(self):
        print('Meow')

A = Person('YB', 'Man')
B = Person('SY', 'Woman')
C = Dog('WJ', 'Female')

Animals = [Person('YB', 'Man'), Dog('H', 'Male'), Cat('SY', 'Female'), Person('JH', 'Woman')]

for i in Animals:
    i.say_something()
