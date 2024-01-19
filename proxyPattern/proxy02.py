# 프록시 패턴 예제
# 백화점에서 현금카드를 사용해서 데님셔츠를 구매해 보자
# 모든 작업을 Bank클래스에서 처리하면 단일 책임의 원칙을 어기게 된다
# Bank의 필수적인 역할은 남겨놓고 DebitCard를 만들어 카드에서 할 수 있는 작업을 부여한다
# 이렇게 하면 Bank가 부가기능을 하는 메서드를 덜어낼 수 있다
# 객체를 생성할 때 한 단계를 더 거치게 되므로 빈번한 객체 생성이 필요한 경우 성능이 저하될 수 있다

from abc import ABCMeta, abstractmethod


# 인터페이스
class Payment(metaclass=ABCMeta):
    @abstractmethod
    def do_pay(self):
        pass


# 실제 객체
class Bank(Payment):
    def __init__(self):
        self.card = None
        self.account = None

    # 카드 소지자의 계좌정보를 조회하는 내부 메서드, 일치하는 계좌의 정보를 넘길 수 있다
    def __getAccount(self):
        self.account = self.card  # 일단 계좌번호와 카드번호는 같습니다
        return self.account

    # 계좌에 충분한 금액이 있는지 확인하는 내부 메서드
    def __hasFunds(self):
        print('Bank :: Checking if Account', self.__getAccount(), 'has enough funds')
        return True

    def setCard(self, card):
        self.card = card

    # 금액 확인 후 결과를 리턴
    def do_pay(self):
        if self.__hasFunds():
            print('Bank :: Paying the merchant')
            return True
        else:
            print('Bank :: Sorry, not enough funds')
            return False


# Proxy(중제자) - Bank클래스의 대리 객체
class DebitCard(Payment):
    # 클라이언트의 요청이 들어오면 내부적으로 실제 객체를 생성
    def __init__(self):
        self.__payWithCard()

    def __payWithCard(self):
        self.bank = Bank()

    def do_pay(self):
        card = input('Proxy :: Punch in Card Number')
        self.bank.setCard(card)
        return self.bank.do_pay()


# 클라이언트
class You:
    # __init__으로 프록시를 호출하고 생성한다.
    def __init__(self):
       print('You :: Lets but the Denim shirt!')
       self.debitCard = DebitCard()
       self.isPurchased = None

    # 내부적으로 proxy메서드를 호출해 금액을 지불한다
    def make_payment(self):
        self.isPurchased = self.debitCard.do_pay()

    # 결제가 끝나고 객체를 소멸 시킨다
    def __del__(self):
        if self.isPurchased:
            print('You :: Denim shirt is Mine!')
        else:
            print('You :: I should earn more :(')


if __name__ == '__main__':
    you = You()
    you.make_payment()
