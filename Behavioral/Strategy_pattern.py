from typing import Protocol


class Strategy(Protocol):
    def execute(self):
        pass


class ConcreteStrategyA(Strategy):
    def execute(self):
        print("Strategy A executed")


class ConcreteStrategyB(Strategy):
    def execute(self):
        print("Strategy B executed")


if __name__ == "__main__":
    strategy = ConcreteStrategyA()
    strategy.execute()

    strategy = ConcreteStrategyB()
    strategy.execute()
