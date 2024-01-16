# PythonDesignPattern

## 객체지향 코드 개발 시 가급적 지켜야 할 원칙(SOLID)
- 단일 책임의 원칙(Single responsibility Principle, SRP)
- 개방 폐쇄 원칙(Open/closed principle, OCP)
- 리스코프 치환 원칙(Liskov substitution principle, LSP)
- 인터페이스 분리의 원칙(Interface segregation principle, ISP)
- 의존 관계 역전의 원칙(Dependency inversion principle, DIP)


### 1. 생성 패턴 (선언된 클래스로 객체를 생성하는 방법)
- 팩토리 메서드 패턴
- 추상 팩토리 패턴
- 빌더 패턴
- 프로토타입 패턴
- 싱글턴 패턴

### 1-1. 팩토리 메서드 패턴
    - 클래스가 직접 객체를 생성하는 것이 아닌, 객체 생성을 위한 팩토리 메서드를 제공
    - 서브 클래스에서 팩토리 메서드를 오버라이드하고 적절한 객체를 생성하도록 함
    - 클래스의 객체 생성 로직을 별도의 클래스로 분리하고 유연성을 확보할 수 있다
    - 단, 클래스의 개수가 증가하게 되어, 클래스가 복잡해질 수 있다
    - 그래서 객체 생성코드가 복잡하지 않거나, 객체 생성이 자주 일어나지 않는 경우엔 부적합

### 1-2. 추상 팩토리 패턴
    - 