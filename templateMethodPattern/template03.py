# 템플릿 메서드 패턴 예제 - 여행사 패키지 추천 서비스
from abc import ABCMeta, abstractmethod


# 여행을 정의하는 추상클래스
class Trip(metaclass=ABCMeta):
    @abstractmethod
    def setTransport(self):
        pass

    @abstractmethod
    def day1(self):
        pass

    @abstractmethod
    def day2(self):
        pass

    @abstractmethod
    def day3(self):
        pass

    @abstractmethod
    def returnHome(self):
        pass

    # 여행일정을 정의하는 메서드(template method)
    def itinerary(self):
        self.setTransport()
        self.day1()
        self.day2()
        self.day3()
        self.returnHome()


# 구체적인 여행일정인 구상클래스
class VeniceTrip(Trip):
    def setTransport(self):
        print("Take a board and find your way in the Grand Canal")

    def day1(self):
        print("Visit St Mark's Basilica in St Mark's Square")

    def day2(self):
        print("Appreciate Doge's Palace")

    def day3(self):
        print("Enjoy the food near the Rialto Bridge")

    def returnHome(self):
        print("Get souvenirs for friends and get back")


class MaldivesTrip(Trip):
    def setTransport(self):
        print("On foot, on any island")

    def day1(self):
        print("Enjoy the marine life of Banana Reef")

    def day2(self):
        print("Go for the water sports and snorkelling")

    def day3(self):
        print("Relax on the beach and enjoy the sun")

    def returnHome(self):
        print("Dont feel like leaving the beach")


class TravelAgency:
    def arrange_trip(self):
        choice = input("What kind of place you'd like to go historical or to a beach?")
        if choice == "historical":
            self.trip = VeniceTrip()
            self.trip.itinerary()
        elif choice == "beach":
            self.trip = MaldivesTrip()
            self.trip.itinerary()


if __name__ == "__main__":
    TravelAgency().arrange_trip()

# 후크
# 후크는 추상클래스에 정의된 메서드이다. 기본구현은 같으나 알고리즘 중간단계를 제어할 수 있는 기능을 제공한다.
# 서브클래스가 반드시 구현해야 하는 부분은 추상메서드를 상요하고 선택적인 부분은 후크를 사용한다.
