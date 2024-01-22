# 상태 패턴 예제 - TV의 On/Off 버튼이 있는 리모컨

from abc import ABCMeta, abstractmethod


class State(metaclass=ABCMeta):
    @abstractmethod
    def doThis(self):
        pass


class StartState(State):
    def doThis(self):
        print("TV Switching ON...")


class StopState(State):
    def doThis(self):
        print("TV Switching OFF...")


# state에 현재상태를 저장하고 현재상태에 맞는 doThis() 메서드를 호출한다.
class TVContext(State):
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def doThis(self):
        self.state.doThis()


if __name__ == "__main__":
    context = TVContext()
    context.getState()

    start = StartState()
    stop = StopState()

    context.setState(stop)
    context.doThis()
