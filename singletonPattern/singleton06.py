# 싱글톤 패턴 사례 2
# 인프라 상태를 확인하는 서비스
# 상태를 확인해야 하는 서버의 목록을 만들고 목록에서 제거된 서버의 상태는 확인하지 않는다.

class HealthCheck:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not HealthCheck._instance:
            HealthCheck._instance = super(HealthCheck, cls).__new__(cls, *args, **kwargs)
        return HealthCheck._instance

    def __init__(self):
        self._servers = []

    def add_server(self):
        self._servers.append('Server 1')
        self._servers.append('Server 2')
        self._servers.append('Server 3')
        self._servers.append('Server 4')

    def change_server(self):
        self._servers.pop()
        self._servers.append('Server 5')


# hc1, hc2는 동일한 객체이다.
hc1 = HealthCheck()
hc2 = HealthCheck()

hc1.add_server()
print('Schedule health check for servers (1)..')
for i in range(4):
    print("Checking ", hc1._servers[i])

# 객체의 동기화
hc2.change_server()
print('Schedule health check for servers (2)..')
for i in range(4):
    print("Checking ", hc2._servers[i])


