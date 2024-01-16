# PythonDesignPattern

## 객체지향 코드 개발 시 가급적 지켜야 할 원칙(SOLID)
- 단일 책임의 원칙(Single responsibility Principle, SRP)
- 개방 폐쇄 원칙(Open/closed principle, OCP)
- 리스코프 치환 원칙(Liskov substitution principle, LSP)
- 인터페이스 분리의 원칙(Interface segregation principle, ISP)
- 의존 관계 역전의 원칙(Dependency inversion principle, DIP)

### 1. 단일 책임의 원칙(SRP)
    클래스 하나에 너무 많은 기능을 넣지 말자
    소프트웨어의 변화 대응을 위해 유지보수성을 극대화 해야 한다
    다른 원칙의 기초철학이 되어 준다

### 2. 개방 폐쇄 원칙(OCP)
    클래스하나를 잘 만들어 놨는데, 새로운 변경사항이 발생했을 때,
    유연하게 코드를 추가 또는 수정할 수 있어야 한다
    클래스는 확장에는 열려있고, 변경에는 닫혀있어야 한다
    대표적으로 추상화 와 다형성이 있다(상속과 관련)
    
### 3. 리스코프 치환 원칙(LSP)
    객체는 프로그램의 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다
    인터페이스 규약을 잘 지켜야 한다
    서브 타입은 기반 타입과 호환이 되어야 한다
    상속을 통한 재사용은 서브와 기반 클래스 사이에 IS-A 관계가 있을 경우로만 제한
    그 외의 경우에는 합성을 이용한 재사용을 해야 한다

### 4. 인터페이스 분리의 원칙(ISP)
    객체 하나를 규정했으면 객체를 사용하는 사용자의 요구에 따라 맞도록 인터페이스를 제공
    인터페이스를 분리했다면, 인터페이스는 가급적 바뀌지 말아야 한다
    인터페이스를 분리하더라도 클라이언트 코드가 변경된다면 분리의 의미가 없다
    클라이언트의 특수성을 고려하여 인터페이스를 작성(클라이언트가 갑이다)

###  5. 의존관계 역전 원칙(DIP)
    구현 클래스(구현체)가 아니라 인터페이스(역할)에 의존해야 한다
    클라이언트가 추상화 된 것에 의존하게 만들고 구상 클래스에 의존하게 만들지 말자
    변수에 구상 클래스의 레퍼런스를 저장하지 말자
    이미있는 기능을 다시 만들지 말자



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
    - 인터페이스를 정의하여 객체 생성을 추상화한 팩토리
    - 추상 팩토리를 클라이언트의 요구에 맞게 팩토리를 구체화시켜 실제 객체를 생성
    - 코드의 유연성을 높이며, 관련 있는 객체들을 쉽게 생성할 수 있다

### 1-3. 빌더 패턴
    - 객체 생성이 복잡한 경우, 단계별로 처리하여 객체를 생성할 수 있다
    - 객체 생성 과정을 단순화하여 코드의 가독성을 높일 수 있다
    - 객체 생성 시 유효성 검사를 수행 할 수 있다
    - 객체 생성 시 생성된 객체의 불변성을 보장할 수 있다
    - 빌더 클래스를 따로 구현해야 해서 코드량이 늘어날 수 있다

### 1-4. 프로토타입 패턴
    - 객체 생성 비용이 큰 경우(DB에서 가져오기 등)
    - 객체를 복제하여 객체 생성에 대한 비용을 줄일 수 있다
    - 객체 생성 과정에서 중복된 코드를 제거할 수 있다
    - 