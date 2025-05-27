from threading import Lock, Thread


class SingletonMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        ...

def run_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value, Singleton._instances)


if __name__ == "__main__":
    # The client code.

    process1 = Thread(target=run_singleton, args=("FOO",))
    process2 = Thread(target=run_singleton, args=("BAR",))
    process1.start()
    process2.start()