# MVC 패턴 구조 - 이메일과 SMS,음성 메시지를 제공하는 클라우드 서비스 구현

# Model - 각 서비스별 요금정보
class Model(object):
    services = {
        'email': {'number': 1000, 'price': 2, },
        'sms': {'number': 1000, 'price': 10, },
        'voice': {'number': 1000, 'price': 15, }
    }


# View - 클라이언트에게 정보를 제공
class View(object):
    def list_services(self, services):
        for svc in services:
            print(svc, ' ')

    def list_pricing(self, services):
        for svc in services:
            print("For", Model.services[svc]['number'],
                  svc, "message you pay $",
                  Model.services[svc]['price'])


# 클라이언트에게 받은 요청을 모델에게 전달하고 리턴받은 데이터를 View에 전달
class Controller(object):
    def __init__(self):
        self.model = Model()
        self.view = View()

    def get_service(self):
        services = self.model.services.keys()
        return self.view.list_services(services)

    def get_pricing(self):
        services = self.model.services.keys()
        return self.view.list_pricing(services)


class Client(object):
    controller = Controller()
    print("Services Provided:")
    controller.get_service()
    print("Pricing for Servics:")
    controller.get_pricing()
