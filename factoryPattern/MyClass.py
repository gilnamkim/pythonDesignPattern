from abc import ABCMeta, abstractmethod


# Product
class Mouse(metaclass=ABCMeta):
    @abstractmethod
    def click_left(self):
        pass

    @abstractmethod
    def click_right(self):
        pass


# concreteProduct
class G102(Mouse):
    def click_left(self):
        print('...click left g102 manufactured by Logitech')

    def click_right(self):
        print('...click right g102 manufactured by Logitech')


class MagicMouse2(Mouse):
    def click_left(self):
        print('...click left magic mouse manufactured by Apple')

    def click_right(self):
        print('...click right magic mouse manufactured by Apple')


# Factory
class MouseFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_mouse(self):
        """
        factory method
        :return:
        """
        pass


# concreteFactory
class LogiMouseFactory(MouseFactory):
    def create_mouse(self):
        return G102()


class AppleMouseFactory(MouseFactory):
    def create_mouse(self):
        return MagicMouse2()


# client
class Client():
    def use(self, company):
        """
        company는 사용자 요구에 따라 변경
        :param company: 제조회사 명
        :return:
        """
        # 사용자 요구에 따라, product를 생산할 factory를 생성
        if company == 'logitech':
            factory = LogiMouseFactory()
        elif company == 'apple':
            factory = AppleMouseFactory()
        else:
            return

        my_mouse = factory.create_mouse()
        my_mouse.click_left()


if __name__ == '__main__':
    client = Client()
    client.use('logitech')
    client.use('apple')
