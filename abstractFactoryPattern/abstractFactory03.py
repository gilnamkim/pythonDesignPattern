from abc import ABCMeta, abstractmethod

from pip._internal.resolution.resolvelib import factory


# 추상 팩토리 : 동물과 색상을 생성하는 인터페이스
class AbstractFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_animal(self):
        pass

    @abstractmethod
    def create_color(self):
        pass


# 추상 제품 : 동물 클래스
class Animal(metaclass=ABCMeta):
    @abstractmethod
    def speak(self):
        pass


# 추상 제품 : 색상 클래스
class Color(metaclass=ABCMeta):
    @abstractmethod
    def fill(self):
        pass


# 구체적인 제품 : 강아지 클래스
class Dog(Animal):
    def speak(self):
        return "멍멍"


# 구체적인 제품 : 고양이 클래스
class Cat(Animal):
    def speak(self):
        return "야옹"


# 구체적인 제품 : 검은색 클래스
class Black(Color):
    def fill(self):
        return "검은색"


# 구체적인 제품 : 갈색 클래스
class Brown(Color):
    def fill(self):
        return "갈색"


# 구체적인 팩토리 : 검정색 강아지를 생성하는 팩토리
class DogBlackFactory(AbstractFactory):
    def create_animal(self):
        return Dog()

    def create_color(self):
        return Black()


# 구체적인 팩토리: 고양이와 갈색을 생성하는 팩토리
class CatBrownFactory(AbstractFactory):
    def create_animal(self):
        return Cat()

    def create_color(self):
        return Brown()


# 클라이언트
class Client:
    def __init__(self, factory):
        self.animal = factory.create_animal()
        self.color = factory.create_color()

    def show(self):
        animal_sound = self.animal.speak()
        color_fill = self.color.fill()
        print(f'{animal_sound} 소리를 내며 {color_fill} 색상을 가진 동물입니다.')


# 클라이언트 코드
dog_black_factory = DogBlackFactory()
cat_brown_factory = CatBrownFactory()

dog_black_client = Client(dog_black_factory)
dog_black_client.show()

cat_brown_client = Client(cat_brown_factory)
cat_brown_client.show()
