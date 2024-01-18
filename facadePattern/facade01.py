class EventManager(object):
    def __init__(self):
        print("Event Manager:: Let me talk to te folks\n")

    def arrange(self):
        self.hotelier = Hotelier()
        self.hotelier.bookHotel()

        self.florist = Florist()
        self.florist.setFlowerRequirements()

        self.caterer = Caterer()
        self.caterer.setCuisine()

        self.musician = Musician()
        self.musician.setMusicType()


class Hotelier(object):
    def __init__(self):
        print("Arranging the Hotel for Marriage? ---")

    def __isAvailable(self):
        print("Is the Hotel free for the event on given day?")
        return True

    def bookHotel(self):
        if self.__isAvailable():
            print("Registered the Booking\n\n")


class Florist(object):
    def __init__(self):
        print("Flower Decorations for the Event? ---")

    def setFlowerRequirements(self):
        print("Carnations, Roses and Lilies would be used for Decoration\n\n")


class Caterer(object):
    def __init__(self):
        print("Food Arrangements for the Event ---")

    def setCuisine(self):
        print("Chinese & Continental Cuisine to be served\n\n")


class Musician(object):
    def __init__(self):
        print("Musical Arrangements for the Marriage ---")

    def setMusicType(self):
        print("Jazz and Classiclal will be played\n\n")


class You(object):
    def __init__(self):
        print("You :: Marriage Arrangements??")

    def askEventManager(self):
        print("You :: Let's Contact the Event Manager\n\n")
        em = EventManager()
        em.arrange()

    def __del__(self):
        print("You :: Thanks to Event Manager, all preparetions done!")


if __name__ == "__main__":
    you = You()
    you.askEventManager()

# EventManager는 You클래스를 위해 인터페이스를 간소화해주는 퍼사드다
# EventManager는 컴포지션을 통해 Hotelier와 Caterer 등의 서브시스템 객체를 생성한다.