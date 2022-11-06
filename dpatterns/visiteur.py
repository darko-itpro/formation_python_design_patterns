class DisplayVisiter:
    def visite_carre(self, carre):
        print("visite du carré")
    def visite_cercle(self, cercle):
        print("visite cercle")

class CalculationVisiter:
    def visite_carre(self, carre):
        print(carre.mesure)
    def visite_cercle(self, cercle):
        print(cercle.mesure)

class Carre:
    mesure = "longueur coté"
    def accept(self, visiteur):
        visiteur.visite_carre(self)


class Cercle:
    mesure = "rayon"
    def accept(self, visiteur):
        visiteur.visite_cercle(self)

Carre().accept(DisplayVisiter())
Cercle().accept(CalculationVisiter())

