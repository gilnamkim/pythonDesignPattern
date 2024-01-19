# 커맨드 패턴 예제
# 증권거래소 구현
from abc import ABCMeta, abstractmethod


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


# ConcreteCommand의 역할을 하는 구상클래스
class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


# Receiver의 역할을 하는 클래스
class StockTrade:
    def buy(self):
        print("You will buy stocks")

    def sell(self):
        print("You will sell stocks")


# StockTrade와 클라이언트 객체 사이의 중개자이며 클라이언트의 요청을 처리한다
class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)
        print("Order OK")
        order.execute()

if __name__ == "__main__":
    # 클라이언트
    stock = StockTrade()
    buyStock = BuyStockOrder(stock)
    sellStock = SellStockOrder(stock)

    # Invoker 중개자
    agent = Agent()
    agent.placeOrder(buyStock)
    agent.placeOrder(buyStock)
    agent.placeOrder(sellStock)
    agent.placeOrder(sellStock)

    # 오더를 캡슐화해서 큐에 저장
    print(agent.__dict__)
