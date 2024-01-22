# 템플릿 메서드 패턴 - iOS기기용 크로스 컴파일러

from abc import ABCMeta, abstractmethod


class Compiler(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileToObject()
        self.run()


class IOSCompiler(Compiler):
    def collectSource(self):
        print("Collecting Swift Source Code")

    def compileToObject(self):
        print("Compiling Swift code to LLVM bitcode")

    def run(self):
        print("Program running on runtime environment")


class AndroidCompiler(Compiler):
    def collectSource(self):
        pass

    def compileToObject(self):
        pass

    def run(self):
        pass


if __name__ == "__main__":
    iOS = IOSCompiler()
    iOS.compileAndRun()
