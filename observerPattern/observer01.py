# 옵저버 패턴의 기본 구조

# subject는 observer를 관리한다 __observers리스트에 observer를 등록
# observer는 register()와 deregister()메서드를 호출해 자신을 등록한다
# observer1,2는 observer인터페이스를 구현해 자신을 subject에 등록한다
# 상태 변화가 있을 때마다 subject는 observer의 알림 메서드를 통해 모든 observer에게 알린다
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def deregister(self, observer):
        self.__observers.remove(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


# subject를 감시하는 객체를 위한 인터페이스 제공
# subject의 상태를 저장한다 subject에 대한 정보와 실제 상태를 일관되게 유지하기 위해 observer 인터페이스를 구현한다
class Observer1:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

    def requestDeregistration(self, subject):
        print(type(self).__name__, ':: remove completed')
        subject.deregister(self)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ':: Got', args, 'From', subject)

    def requestDeregistration(self, subject):
        print(type(self).__name__, ':: remove completed')
        subject.deregister(self)


subject = Subject()
observer1 = Observer1(subject)
observer2 = Observer2(subject)
subject.notifyAll('notification')
observer1.requestDeregistration(subject)
print('==' * 50)
subject.notifyAll('notification')
