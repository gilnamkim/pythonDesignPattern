# 모노스테이트 싱글톤 패턴
# 모든 객체가 같은 상태(모노스테이트)를 공유하는 패턴

class Borg:
    _shared_state = {'x': '1'}

    def __init__(self):
        self.x = 1
        self.__dict__ = self._shared_state
        pass


# __new__ 메서드를 사용하여 구현하는 방법
class Borg2(object):
    _share_state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Borg2, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._share_state
        return obj


b1 = Borg()
b2 = Borg()
b1.y = '2'
b2.x = '5'

print("Borg Object 'b1': ", b1)  # b1과 b2는 다른 객체이다.
print("Borg Object 'b2': ", b2)
print("Object State 'b1': ", b1.__dict__)  # b1 과 b2는 상태를 공유한다
print("Object State 'b2': ", b2.__dict__)
