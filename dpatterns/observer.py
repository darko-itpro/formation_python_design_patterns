from abc import ABC, abstractmethod

class Observer(ABC):

    @abstractmethod
    def update(self, data):
        pass

class Observable:
    def __init__(self):
        self.observers = []
    def add_observer(self, observer: Observer):
        self.observers.append(observer)
    def remove_observer(self, observer: Observer):
        self.observers.remove(observer)
    def notify(self, data):
        for o in self.observers:
            o.update(data)

class Component(Observer):
    def __init__(self, name):
        self.name = name
        self.listeners = []
    def update(self, data):
        print(f"Mise à jour de {self.name} avec {data}")

observable = Observable()
observable.add_observer(Component("Observer 1"))
observable.add_observer(Component("Observer 2"))
observable.add_observer(Component("Observer 3"))

observable.notify("Des données")
