from abc import ABCMeta, abstractmethod


class Building(metaclass=ABCMeta):
    @abstractmethod
    def build(self):
        pass


class EuropeStyle(Building):
    def build(self):
        print("유럽스타일 건물")


class KoreanStyle(Building):
    def build(self):
        print("한국스타일 건물")


class ConstructionFirm(metaclass=ABCMeta):
    @abstractmethod
    def name(self):
        pass


class EuropeConstructionFirm(ConstructionFirm):
    def name(self):
        return EuropeStyle()


class KoreanConstructionFirm(ConstructionFirm):
    def name(self):
        return KoreanStyle()


class Client():
    def use(self, construction):
        if construction == 'euro':
            factory = EuropeConstructionFirm()
        elif construction == 'korea':
            factory = KoreanConstructionFirm()
        else:
            return

        my_building = factory.name()
        my_building.build()



if __name__ == '__main__':
    client = Client()
    client.use('korea')
    client.use('euro')
