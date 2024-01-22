# 상태 패턴 예제 - 컴퓨터 시스템(On/Off/일시중지/절전)상태 구현

from abc import ABCMeta, abstractmethod


class ComputerState(metaclass=ABCMeta):
    name = "state"
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print("Current:", self, " => switched to new state", state.name)
            self.__class__ = state
        else:
            print("Current:", self, " => switching to", state.name, "not possible")

    def __str__(self):
        return self.name


class Off(ComputerState):
    name = 'off'
    allowed = ['on']


class On(ComputerState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputerState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputerState):
    name = 'hibernate'
    allowed = ['on']


class Computer(object):
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def getState(self):
        return self.state

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()
    # 전원 ON
    comp.change(On)
    # 전원 OFF
    comp.change(Off)

    # 전원 ON
    comp.change(On)
    # 일시 중지
    comp.change(Suspend)
    # 절전모드 변경 불가
    comp.change(Hibernate)
    # 전원 OFF 불가
    comp.change(Off)
    # 전원 ON
    comp.change(On)
    # 전원 OFF
    comp.change(Off)
    # 현재 상태
    print(f'Current: {comp.getState()}')
