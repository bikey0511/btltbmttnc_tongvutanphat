# Phương thức trong lớp
class Calculation:
    def add(self, a, b):
        return a + b
    def add (self, a ,b ,c):
        return a + b + c

class Animal:
            def make_sound(self ):
                return " Generic sound"
class Dog(Animal):
            def make_sound(self):
                return"Woof!"
class Animal:
    def make_sound(self):
        return "Generic sound"
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
def animal_sound(animal):
    return animal.make_sound()
dog = Dog()
cat = Cat()
print(animal_sound(dog))  # Kết quả: Woof!
print(animal_sound(cat))  # Kết quả: Meow!