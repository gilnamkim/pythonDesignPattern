# 템플릿 메서드 패턴의 기본 구조
from abc import ABCMeta, abstractmethod


# 알고리즘의 각 단계를 정의하는 추상 메서드
class AbstractClass(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def operation1(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    # 알고리즘의 뼈대를 정의한다. 전체 알고리즘을 정의하는 여러 추상 메서드를 호출한다.
    def template_method(self):
        print("Defining the Algorithm. Operation1 follows Operation2")
        self.operation2()
        self.operation1()


# 알고리즘의 서브클래스를 구현
class ConcreteClass(AbstractClass):
    def operation1(self):
        print("My Concrete Operation1")

    def operation2(self):
        print("Operation2 remains same")


class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


if __name__ == "__main__":
    client = Client()
    client.main()
