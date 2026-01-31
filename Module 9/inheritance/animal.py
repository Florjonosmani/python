from tensorflow.compiler.tf2xla.python.xla import self_adjoint_eig


class Animal:

    def sound(self):
        print("some generic animal sound")

class Dog(Animal):

    def sound(self):
        print("Woof! Woof!")

class Cat(Animal):
    def sound(self):
     print("MEOWWWWWWWWWWWWWWW! MEOWWWWWW!")

animal = Animal()
animal.sound()

dog = Dog()
dog.sound()

cat = Cat()
cat.sound()