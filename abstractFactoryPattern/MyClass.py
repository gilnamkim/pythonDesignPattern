from abc import ABCMeta, abstractmethod


# (abstract)Product
class Keyboard(metaclass=ABCMeta):
    @abstractmethod
    def type_words(self):
        pass


class Mouse(metaclass=ABCMeta):
    @abstractmethod
    def click_left(self):
        pass


# concreteProduct
class K380(Keyboard):
    def type_words(self):
        print('...type with k380 manufactured by Logitech')


class MagicKeyboard(Keyboard):
    def type_words(self):
        print('...type with magic keyboard manufactured by Apple')


class G102(Mouse):
    def click_left(self):
        print('...click left g102 manufactured by Logitech')


class MagicMouse2(Mouse):
    def click_left(self):
        print('...click left magic mouse manufactured by Apple')


# (abstract)Factory
class ComputerFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_keyboard(self):
        pass

    @abstractmethod
    def create_mouse(self):
        pass


# concreteFactory
class LogitechComputerFactory(ComputerFactory):
    def create_keyboard(self):
        return K380()

    def create_mouse(self):
        return G102()


class AppleComputerFactory(ComputerFactory):
    def create_keyboard(self):
        return MagicKeyboard()

    def create_mouse(self):
        return MagicMouse2()


# client
class Client():
    def use(self, company):
        """
        :param company: 제조사 이름(사용자 요구에 따라 변경)
        :return:
        """

        # product를 생산할 factory 생성
        if company == 'Logitech':
            factory = LogitechComputerFactory()
        elif company == 'Apple':
            factory = AppleComputerFactory()
        else:
            return

        # product 생산(객체 생성)
        keyboard = factory.create_keyboard()
        mouse = factory.create_mouse()

        # 생산된 product를 사용
        keyboard.type_words()
        mouse.click_left()


if __name__ == '__main__':
    client = Client()
    client.use('Logitech')
    print()
    client.use('Apple')