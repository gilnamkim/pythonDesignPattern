class Animal():
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("I am a dog")


class Cat(Animal):
    def speak(self):
        print("I am a cat")


class AnimalFactory():
    def createAnimal(self):
        pass


class DogFactory(AnimalFactory):
    def haveDog(self):
        self.dog = self.createAnimal()

    def createAnimal(self):
        return Dog()

    def makeWings(self, dog: Dog):
        print('dog wings added')
        return dog


class CatFactory(AnimalFactory):
    def __init__(self):
        self.cat_count = 0

    def createAnimal(self):
        self.cat_count += 1
        return Cat()

    def catCount(self):
        return self.cat_count


if __name__ == '__main__':
    cat_factory = CatFactory()
    cat = cat_factory.createAnimal()
    print(f'{cat_factory.catCount()} cats are created')

    dog_factory = DogFactory()
    dog = dog_factory.createAnimal()
    wing_dog = dog_factory.makeWings(dog)
