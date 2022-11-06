"""
Illustration d'un singlethon *pythonique* utilisant `__dict__`.
"""

class Borg:
    _shared = {}

    def __init__(self):
        self.__dict__ = self._shared


seven_of_nine = Borg()
locutus = Borg()

seven_of_nine.value = 42

print(locutus.value)
