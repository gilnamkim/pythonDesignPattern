# 커맨드 패턴을 사용한 인스톨러 구현
# 커맨드 패턴은 Command, Receiver, Invoker, Client 클래스로 구성된다.

# Wizard 객체 = Command
class Wizard(object):
    def __init__(self, src, rootdir):
        self.choices = []
        self.rootdir = rootdir
        self.src = src

    # preferences() = Receiver
    def preferences(self, command):
        self.choices.append(command)

    # execute() = Invoker
    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print("Copying binaries --", self.src, " to ", self.rootdir)
            else:
                print("No Operation")


# Client
if __name__ == "__main__":
    # 객체 생성
    wizard = Wizard("python3.5.gzip", "/usr/bin/")

    # 옵션 선택
    wizard.preferences({'python': True})
    wizard.preferences({'java': False})

    # 실행
    wizard.execute()
