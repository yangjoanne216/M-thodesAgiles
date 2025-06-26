from .Person import Person


class Acteur(Person):
    def __init__(self, nom):
        self.nom = nom
        self.serie = None
        self.role = None

    def setRole(self, role):
        self.role = role

    def getRole(self):
        return self.role

    def setSerie(self, serie):
        self.serie = serie
        serie.set_acteur(self)

    def getNom(self):
        return self.nom

    def getSerie(self):
        return self.serie

    def introduce(self) -> str:
        if self.role is not None:
            return self.role.introduce()
        return "Je suis un acteur, mon nom est " + self.nom
