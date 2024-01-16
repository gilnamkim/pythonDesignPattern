# 계산기 연산 처리 클래스
class Operation:
    def operate(self, x, y):
        pass


# 덧셈 연산 클래스
class AddOperation(Operation):
    def operate(self, x, y):
        return x + y


# 뺄셈 연산 클래스
class SubtractOperation(Operation):
    def operate(self, x, y):
        return x - y


# 곱셈 연산 클래스
class MultiplyOperation(Operation):
    def operate(self, x, y):
        return x * y


# 나눗셈 연산 클래스
class DivideOperation(Operation):
    def operate(self, x, y):
        return x / y


# 팩토리 메서드
class OperationFactory:
    @staticmethod
    def create_operation(operator):
        if operator == '+':
            return AddOperation()
        elif operator == '-':
            return SubtractOperation()
        elif operator == '*':
            return MultiplyOperation()
        elif operator == '/':
            return DivideOperation()
        else:
            raise ValueError('Invalid operator')


# 사용 예시
if __name__ == '__main__':
    x = 10
    y = 5

    # 덧셈 연산 객체 생성 및 처리
    add_operation = OperationFactory.create_operation('+')
    result = add_operation.operate(x, y)
    print(f'{x} + {y} = {result}')

    # 나눗셈 연산 객체 생성 및 처리
    divide_operation = OperationFactory.create_operation('/')
    result = divide_operation.operate(x, y)
    print(f'{x} / {y} = {result}')
