# 개으른 초기화(Lazy instantiation)
# 모듈을 임포트할 때 아직 필요하지 않은 시점에 객체가 미리 생성되는 것을 방지한다.
# getInstance()메서드로 꼭 필요할 때 객체를 생성할 수 있다.
# 사용가능한 리소스가 제한적인 경우 유용하다.

class Singleton(object):
    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('__init__ method called...')
        else:
            print('Instance already created:', self.getInstance())

    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance


s = Singleton()   # 클래스를 초기화 했지만 객체는 생성하지 않음
print('Object created', Singleton.getInstance())  # 객체 생성
s1 = Singleton()  # 객체는 이미 생성됐음
