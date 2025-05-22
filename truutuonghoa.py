from abc import ABC, abstractmethod
class AbstractAnimal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
class AbstractDog(AbstractAnimal):
    def make_sound(self):
        return "Woof!"
class AbstractCat(AbstractAnimal):
    def make_sound(self):
        return "Meow!"
abstract_dog = AbstractDog()
abstract_cat = AbstractCat()
print(abstract_dog.make_sound()) 
print(abstract_cat.make_sound()) 