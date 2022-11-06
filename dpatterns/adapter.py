class Chien:
    def aboyer(self):
        print("Ouaf")

class Chat:
    def miauler(self):
        print('Miaou')

class Cheval:
    def hennir(self):
        print('Hiiii')

class Cochon:
    def grogner(self):
        print('Gruik')

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def faire_bruit(self):
        pass

class ChienAlternate(Animal, Chien):
    def faire_bruit(self):
        return self.aboyer()


class ChatAlternate(Animal, Chat):
    faire_bruit = Chat.miauler

class ChevalAlternate(Animal):
    def __init__(self, cheval):
        self.cheval = cheval
    def faire_bruit(self):
        return self.cheval.hennir()
    def __getattr__(self, attr):
        return self.cheval.__getattr__(attr)

class CochonAdapter:
    def __init__(self, cochon):
        self.cochon = cochon
    def __getattr__(self, attr):
        if attr == 'faire_bruit':
            return self.cochon.grogner
        return getattr(self.cochon, attr)
