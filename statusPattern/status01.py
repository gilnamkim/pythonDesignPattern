# 상태 패턴 기본 구조
from abc import ABCMeta, abstractmethod


# 객체의 행동을 캡슐화하는 인터페이스
class State(metaclass=ABCMeta):
    @abstractmethod
    def Handle(self):
        pass


# 객체의 행동을 구현
class ConcreteStateB(State):
    def Handle(self):
        print("ConcreteStateB")


class ConcreteStateA(State):
    def Handle(self):
        print("ConcreteStateA")


# 사용자의 요청에 따라 객체의 현재상태(Context.state)에 따라 요청을 수행
class Context(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def Handle(self):
        self.state.Handle()


if __name__ == "__main__":
    context = Context()
    stateA = ConcreteStateA()
    stateB = ConcreteStateB()

    context.setState(stateA)
    context.setState(stateB)
    context.Handle()
