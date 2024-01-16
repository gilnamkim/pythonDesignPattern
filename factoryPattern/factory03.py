from enum import Enum


class AnimalEnum(Enum):
    CAT = 1
    DOG = 2
    COW = 3


class Animal():
    def speak(self):
        pass


class Cat(Animal):
    def speak(self):
        print("I am a cat")


class Dog(Animal):
    def speak(self):
        print("I am a dog")


class Cow(Animal):
    def speak(self):
        print("I am a cow")


# factory function
# prefer enum
def FactoryFn(animal: AnimalEnum):
    if animal == AnimalEnum.CAT:
        return Cat()
    elif animal == AnimalEnum.DOG:
        return Dog()
    elif animal == AnimalEnum.COW:
        return Cow()


if __name__ == "__main__":
    cat = FactoryFn(AnimalEnum.CAT)
    dog = FactoryFn(AnimalEnum.DOG)
    cow = FactoryFn(AnimalEnum.COW)
    cat.speak()
    dog.speak()
    cow.speak()


