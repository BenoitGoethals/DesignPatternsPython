from typing import Protocol


class Subject:
    def __init__(self):
        self._observers = []
        self._state = None

    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, value):
        self._state = value
        self.notify()


class Observer(Protocol):
    def update(self, sub: Subject):
        pass


class ConcreteObserverA(Observer):
    def update(self, sub: Subject):
        print(f"ObserverA: Reacted to state change -> {sub.state}")


class ConcreteObserverB(Observer):
    def update(self, sub: Subject):
        print(f"ObserverB: Received update -> {sub.state}")


# Gebruik
subject = Subject()

observer_a = ConcreteObserverA()
observer_b = ConcreteObserverB()

subject.attach(observer_a)
subject.attach(observer_b)

subject.state = "State 1"
# Output:
# ObserverA: Reacted to state change -> State 1
# ObserverB: Received update -> State 1

subject.state = "State 2"
# Output:
# ObserverA: Reacted to state change -> State 2
# ObserverB: Received update -> State 2
