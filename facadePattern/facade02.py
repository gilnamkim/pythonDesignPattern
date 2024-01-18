# * 파사드 디자인 패턴의 최소 지식 원칙
#     - 시스템을 설계할 때 생성하는 모든 객체가 몇 개의 클래스와 연관되며 어떤식으로 대화하는지 알아야 한다.
#     - 원칙에 따라 지나치게 서로 얽혀있는 클래스를 만드는 것을 지양해야 한다.
#     - 클래스 간의 의존도가 높아지면 유지보수가 힘들어진다. 시스템의 한 부분을 수정할 때 다른 부분이 의도치 않게 변경되지 않게 해야 한다.
#
# * 데메테르의 법칙과 파사드 패턴
# 여러개의 .(dot)을 사용하면 객체,클래스 간 의존도(결합도)가 높아져 유지보수하기 힘들어 진다.
# 객체의 내부 구조를 외부로 드러내지 않는 것이 중요하다.
# 규칙화를 하기위해서 객체의 모든 메서드는 다음에 해당하는 메서드만 호출해야 한다.
# 1. 객체 자신의 메서드
# 2. 메서드의 파라미터로 넘어온 객체들의 메서드
# 3. 메서드 내부에서 생성, 초기화 된 객체의 메서드
# 4. 인스턴스 변수로 가지고 있는 객체가 소유한 메서드
