# 싱글톤 패턴 사례 1
# 여러 서비스가 하나의 DB를 공유하는 구조
# 데이터베이스 작업 간에 일관성이 유지돼야 한다. 작업 간 충돌X
# 다수의 DB연산을 처리하려면 리소스를 효율적으로 사용해야 한다

import sqlite3


# 메타클래스 생성
class MetaSingleton(type):
    _instances = {}

    # __call__ 메서드를 통해 싱글톤을 생성한다.
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


# Database 클래스를 init하면 하나의 객체가 생성된다.
class Database(metaclass=MetaSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = sqlite3.connect('db.splite3')
            self.cursorobj = self.connection.cursor()
            print("Connected")
        return self.cursorobj


# Database클래스의 connect를 요청하여 클래스가 초기화되지만 내부적으로 db1, db2에 대한 하나의 객체만 생성된다.
# 따라서 데이터베이스(객체)에 대한 작업은 모두 동기화된다.
# 또한 다수의 요청에 객체를 하나만 만듦으로 리소스가 절약된다.
# 단, 하나의 클라이언트가 여러번 요청하는 작업에 적합하며, 다수의 클라이언트가 요청하는 경우 연결 풀링 기법이 더 효율적이다.
db1 = Database().connect()
db2 = Database().connect()

print('Database Object DB1', db1)
print('Database Object DB2', db2)
