# PythonDesignPattern

## 객체지향 코드 개발 시 가급적 지켜야 할 원칙(SOLID)
- 단일 책임의 원칙(Single responsibility Principle, SRP)
- 개방 폐쇄 원칙(Open/closed principle, OCP)
- 리스코프 치환 원칙(Liskov substitution principle, LSP)
- 인터페이스 분리의 원칙(Interface segregation principle, ISP)
- 의존 관계 역전의 원칙(Dependency inversion principle, DIP)

### 단일 책임의 원칙(SRP)
    클래스 하나에 너무 많은 기능을 넣지 말자
    소프트웨어의 변화 대응을 위해 유지보수성을 극대화 해야 한다
    다른 원칙의 기초철학이 되어 준다

### 개방 폐쇄 원칙(OCP)
    클래스하나를 잘 만들어 놨는데, 새로운 변경사항이 발생했을 때,
    유연하게 코드를 추가 또는 수정할 수 있어야 한다
    클래스는 확장에는 열려있고, 변경에는 닫혀있어야 한다
    대표적으로 추상화 와 다형성이 있다(상속과 관련)
    
### 리스코프 치환 원칙(LSP)
    객체는 프로그램의 정확성을 깨지 않으면서 하위 타입의 인스턴스로 바꿀 수 있어야 한다
    인터페이스 규약을 잘 지켜야 한다
    서브 타입은 기반 타입과 호환이 되어야 한다
    상속을 통한 재사용은 서브와 기반 클래스 사이에 IS-A 관계가 있을 경우로만 제한
    그 외의 경우에는 합성을 이용한 재사용을 해야 한다

### 인터페이스 분리의 원칙(ISP)
    객체 하나를 규정했으면 객체를 사용하는 사용자의 요구에 따라 맞도록 인터페이스를 제공
    인터페이스를 분리했다면, 인터페이스는 가급적 바뀌지 말아야 한다
    인터페이스를 분리하더라도 클라이언트 코드가 변경된다면 분리의 의미가 없다
    클라이언트의 특수성을 고려하여 인터페이스를 작성(클라이언트가 갑이다)

### 의존관계 역전 원칙(DIP)
    구현 클래스(구현체)가 아니라 인터페이스(역할)에 의존해야 한다
    클라이언트가 추상화 된 것에 의존하게 만들고 구상 클래스에 의존하게 만들지 말자
    변수에 구상 클래스의 레퍼런스를 저장하지 말자
    이미있는 기능을 다시 만들지 말자



### 1. 생성 패턴 (선언된 클래스로 객체를 생성하는 방법)
    <특징>
    - 객체가 생성되는 방식을 기반으로 작동한다
    - 객체 생성 관련 상세 로직을 숨긴다
    - 코드와 생성되는 객체의 클래스는 서로 독립적이다

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

### 1-5. 싱글턴 패턴
    - 하나의 클래스에 대해 단 하나의 객체만 생성한다
    - 고정된 메모리영역을 얻어 하나의 객체를 생성하기 때문에 메모리낭비를 방지한다
    - 객체가 전역적으로 사용될 수 있기에 다른 클래스의 객체들이 데이터를 공유하고 변경할 수 있다
    - 너무 많은 작업을 위임하거나 데이터를 공유시킬 경우 다른 객체간의 결합도가 높아진다
    - 멀티스레드 환경에서 데이터 동기화 문제가 발생할 수 있다

### 2. 구조 패턴
    <특징>
    - 클래스와 객체를 더 큰 결과물로 합칠 수 있는 구조로 설계한다
    - 구조가 단순해지고, 클래스와 객체 간의 상호관계를 파악할 수 았다
    - 클래스 상속과 컴포지션에 의존한다

- 어댑터 패턴
- 브릿지 패턴
- 복합체 패턴
- 데코레이터 패턴
- 퍼사드 패턴
- 플라이웨이트 패턴
- 프록시 패턴

### 2-1. 퍼사드 패턴
    - 복잡한 내부 시스템 로직을 감추고 클라이언트가 쉽게 시스템이 접근할 수 있는 인터페이스 제공
    - 서브시스템의 인터페이스를 통합시킨 단일 인터페이스를 제공한다
    - 단일 인터페이스 객체로 복잡한 서브시스템을 대체한다
    - 서브시스템을 캡슐화하지 않고 모든 서브시스템들을 결합한다
    - 클라이언트와 내부 구현을 분리한다
    - ex) 웨딩플래너(퍼사드)가 결혼식(클라이언트)을 위해 관련업체(시스템)와 준비를 한다

### 2-2. 프록시 패턴
    - 프록시란 요청자와 공급자 사이의 중재자를 의미한다
    - 복잡한 시스템을 간단하게 표현할 수 있어야 한다
    - 객체에 대한 보안을 제공한다. 클라이언트는 객체에 직접 접근할 수 없다
    - 다른 서버에 존재하는 외부 객체에 대한 로컬 인터페이스를 제공한다
    - 메모리 사용량이 높은 객체를 다루는 가벼운 핸들러 역할을 한다. 메인 객체가 반드시 필요한 경우 생성 가능

### 3. 행동 패턴
    <특징>
    - 객체 간의 상호작용과 책임을 기반으로 작동한다
    - 객체는 상호작용하지만 느슨하게 결합돼야 한다

### 3-1. 옵저버 패턴
    - 옵저버는 객체의 상태에 따라 자신의 객체 상태를 변경하거나 필요한 연산을 수행
    - 객체 간 1대N 관계를 형성하고 객체의 상태를 다른 종속 객체에 자동으로 알린다
    - 객체의 핵심부분을 캡슐화한다
    - 종속된 서비스가 코어 서비스의 상태를 참고하는 구조에 적합하다

### 3-2. 커맨드 패턴
    - 객체가 특정 기능을 바로 수행하거나 나중에 트리거할 때 필요한 모든 정보를 캡슐화하는 패턴
    - 캡슐화하는 정보는 메서드명, 메서드를 소유하는 객체, 메서드 인자
    - ex) 인스톨 위저드 - 단계별로 선택한 설정을 Command 객체에 저장하여 Finish 때 저장된 설정으로 수행
    -  즉 모든 설정을 추후에 함수를 호출할 객체 속에 캡슐화하는 구조
    - 수행할 명령에 따라 객체를 변수화할 때 적합

### 3-3. 템플릿 메서드 패턴
    - 알고리즘의 일부 단계를 서브클래스화해 알고리즘의 부분적 수정 및 재정의를 쉽게 한다.
    - 여러 알고리즘 또는 클래스가 비슷하거나 같은 로직을 구현할 때 적합
    - 알고리즘을 단계별로 서브클래스화해 코드의 중복을 줄일 수 있는 경우
    - 서브클래스를 오버라이드해 여러 알고리즘을 구현할 수 있는 경우


## 컴파운드 패턴
- 여러가지의 패턴을 복합적으로 사용하여 일반적인 문제를 해결하는 패턴
- 복합적으로 사용된 패턴들이 다른 디자인 패턴처럼 일반적인 문제를 해결할 수 있어야 컴파운드 패턴이다
- 대표적으로 MVC, MVP, MVVM 패턴이 있다


