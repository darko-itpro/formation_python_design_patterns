from threading import Lock, Thread
import time

class Singleton:
    _instance = None
    _lock = Lock()

    value: str = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, value: str) -> None:
        self.value = value

    def some_business_logic(self):
        ...

def run_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value, id(singleton))


if __name__ == "__main__":
    # The client code.

    process1 = Thread(target=run_singleton, args=("FOO",))
    process2 = Thread(target=run_singleton, args=("BAR",))
    process1.start()
    process2.start()