class Componant:
    def __init__(self, name, conditions):
        self.name = name
        self.conditions = conditions
        self.next = None

    def set_next(self, next):
        self.next = next

    def process(self, condition, message):
        if condition in self.conditions:
            print(f'Traitement de {message} par {self.name}')

        if self.next is not None:
            self.next.process(condition, message)

c1 = Componant("Co 1", ["mail", "phone"])
c2 = Componant("Co 2", ["mail"])
c3 = Componant("Co 3", ["phone"])

c1.set_next(c2)
c2.set_next(c3)

c1.process("mail", "Send mail")
c1.process("phone", "Call him")
