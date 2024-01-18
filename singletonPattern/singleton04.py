# 싱글톤과 메타클래스
# 메타클래스를 사용하면 이미 정의된 파이썬 클래스를 통해 새로운 형식의 클래스를 생성할 수 있다.

class MyInt(type):
    def __call__(cls, *args, **kwargs):
        print('***** Here is My int *****', args)
        print('Now do whatever you want with these objects...')
        return type.__call__(cls, *args, **kwargs)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


# i = int(4, 5)


# 클래스 생성과 겍체 초기화를 더 세부적으로 제어
class MetaSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
logger1.x = '1'
logger2.y = '2'
print(logger1.__dict__)
print(logger1 is logger2)
print(logger2.__dict__)
