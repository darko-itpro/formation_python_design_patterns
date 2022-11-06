from abc import ABC, abstractmethod

class Composant(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def verbose(self, level=0):
        return

class Feuille(Composant):
    def verbose(self, level=0):
        return f"{'    ' * level} - {self.name}"

class Composite(Composant):
    def __init__(self, name):
        Composant.__init__(self, name)
        self.contenu = []
    def add(self, composant):
        self.contenu.append(composant)
    def verbose(self, level=0):
        feuilles = [f.verbose(level+1) for f in self.contenu]
        feuilles.insert(0, f'{"    " * level} * {self.name}')
        return '\n'.join(feuilles)

s1 = Composite('Anakin Skywalker')
s1.add(Feuille('La Menace Fantôme'))
s1.add(Feuille("L'Attaque des Clones"))
s1.add(Feuille('La Revenchez des Siths'))

s2 = Composite('Luke Skywalker')
s2.add(Feuille('Un Nouvel Espoir'))
s2.add(Feuille("L'Empire Contre-Attaque"))
s2.add(Feuille('Le Retour du Jedi'))

s3 = Composite('Ray Palpatine Skywalker')
s3.add(Feuille('Le Réveil de la Force'))
s3.add(Feuille('Le Dernier Jedi'))
s3.add(Feuille("L'ascension de Skywalker"))

sw = Composite('Star Wars')
sw.add(s1)
sw.add(Feuille('Rogue One'))
sw.add(s2)
sw.add(s3)

print(sw.verbose())

print('-----')

print(s2.verbose())