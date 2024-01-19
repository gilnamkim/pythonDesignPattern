# 배우와 에이전트와의 관계
# 영화 제작사(클라이언트)는 보통 배우(main instance)에게 직접 접근하지 않고 에이전트(proxy)에게 출연 제의를 준다.
# 에이전트는(proxy) 배우를 대신해 스케줄과 출연료를 조율한다.
# proxy객체를 통해


# 메인 객체인 배우
class Actor(object):
    def __init__(self):
        self.isBusy = None

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")  # 다른 영화 촬영 중

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")  # 출연 가능

    def getStatus(self):
        return self.isBusy


# 프록시(proxy)의 역할을 하는 에이전트
class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self, actor):
        self.actor = actor
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


# 클라이언트
if __name__ == "__main__":
    r = Agent()
    tom = Actor()

    r.work(tom)
    tom.isBusy = True

    r.work(tom)



