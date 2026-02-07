


class Animal:
    def __init__(self,name):
        self.name = name

    def sound(self):
        print('some generic animal sound')

    def description(self):
        print(f"this is an animal named{self.name}.")

class Dog(Animal):
    def __init__(self,name,breed):
        super(). __init__(name)
        self.name = name
        self.breed = breed

    def sound(self):
        print('RUF! RUF GRRR!')

    def description(self):
        super().description()
        print(f"Breed: {self.breed}")

class Cat(Animal):
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color

    def sound(self):
        print('meow! meow!')


    def description(self):
        super().description()
        print(f"Color: {self.color}")

animal = Animal("Generic Animal")
animal.sound()
animal.description()

dog =Dog("Rex","Vuqiak")
dog.sound()
dog.description()

cat = Cat("Whiskers", "orange")
cat.sound()
cat.description()