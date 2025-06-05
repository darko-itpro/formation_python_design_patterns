from abc import ABC, abstractmethod

class GeometricVisiter(ABC):
    @abstractmethod
    def visite_carre(self, carre):
        pass

    @abstractmethod
    def visite_cercle(self, cercle):
        pass

class DisplayVisiter(GeometricVisiter):
    def visite_carre(self, carre):
        print("visite du carré")
    def visite_cercle(self, cercle):
        print("visite cercle")

class CalculationVisiter(GeometricVisiter):
    def visite_carre(self, carre):
        print(carre.mesure)
    def visite_cercle(self, cercle):
        print(cercle.mesure)

class Carre:
    mesure = "longueur coté"
    def accept(self, visiteur:GeometricVisiter):
        visiteur.visite_carre(self)


class Cercle:
    mesure = "rayon"
    def accept(self, visiteur:GeometricVisiter):
        visiteur.visite_cercle(self)

Carre().accept(DisplayVisiter())
Cercle().accept(CalculationVisiter())

