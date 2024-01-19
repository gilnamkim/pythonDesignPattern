# 옵저버 패턴 예제
# 뉴스 에이전시 구현, 여러 곳에서 뉴스를 모아 구독자에게 전달한다

from abc import ABCMeta, abstractmethod


# 뉴스 게시자 구현
class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latesNews = None

    # 구독추가 메서드(Insert)
    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    # 구독제거 메서드(Remove)
    def detach(self):
        return self.__subscribers.pop()

    # 구독목록 반환(List)
    def subscriber(self):
        return [type(x).__name__ for x in self.__subscribers]

    # 구독목록에게 뉴스알람
    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    # 파라미터로 받은 새로운 뉴스를 저장
    def addNews(self, news):
        self.__latesNews = news

    # 마지막으로 저장된 뉴스를 리턴
    def getNews(self):
        return "Got News:", self.__latesNews


# observer 인터페이스
# 모든 종류의 구현클래스의 추상클래스
class Subscriber(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


# Subscriber의 구현 클래스
class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber(Subscriber):
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == "__main__":
    news_publisher = NewsPublisher()
    for Subscriber in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        Subscriber(news_publisher)
    print("\nSubscribers:", news_publisher.subscriber())

    news_publisher.addNews("Hello World!")
    news_publisher.notifySubscribers()

    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nDetached:", type(news_publisher.detach()).__name__)
    print("\nSubscribers:", news_publisher.subscriber())

    news_publisher.addNews("My second news!")
    news_publisher.notifySubscribers()

