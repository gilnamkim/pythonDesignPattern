# 커맨드 패턴 예제 - 커맨드 패턴 구조
from abc import ABCMeta, abstractmethod


# 연산을 수행할 인터페이스 정의
class Command(metaclass=ABCMeta):
    def __init__(self, recv):
        self.recv = recv

    @abstractmethod
    def execute(self):
        pass


# Receiver 객체와 연산(action()) 간 바인딩
class ConcreteCommand(Command):
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        self.recv.action()


# 요청에 관련된 연산을 관리
class Receiver:
    def action(self):
        print("Receiver Action")


# ConcreteCommand에 수행을 요청
class Invoker:
    # 요청을 받아 캡슐화해 큐에 넣는다.
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


# Client ConcreteCommand객체를 생성하고 Receiver를 설정한다
if __name__ == "__main__":
    recv = Receiver()
    cmd = ConcreteCommand(recv)  # Receiver에게 요청을 넘김

    invoker = Invoker()
    invoker.command(cmd)  # 요청을 캡슐화

    invoker.execute()
