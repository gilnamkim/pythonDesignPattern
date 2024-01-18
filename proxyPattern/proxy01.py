# 배우와 에이전트와의 관계
# 영화 제작사(클라이언트)는 보통 배우(main instance)에게 직접 접근하지 않고 에이전트(proxy)에게 출연 제의를 준다.
# 에이전트는(proxy) 배우를 대신해 스케줄과 출연료를 조율한다.
# proxy객체를 통해

class Actor(object):
    def __init__(self):
        self.isBusy = True

    def occupied(self):
        self.isBusy = True
        print(type(self).__name__, "is occupied with current movie")  # 다른 영화 촬영 중

    def available(self):
        self.isBusy = False
        print(type(self).__name__, "is free for the movie")  # 출연 가능

    def getStatus(self):
        return self.isBusy


class Agent(object):
    def __init__(self):
        self.principal = None

    def work(self):
        self.actor = Actor()
        if self.actor.getStatus():
            self.actor.occupied()
        else:
            self.actor.available()


if __name__ == "__main__":
    r = Agent()
    r.work()

