class Acteur:
    def __init__(self, nom):
        self.nom = nom
        self.serie = None

    def setSerie(self, serie):
        self.serie = serie
        serie.set_acteur(self)  # ✅ 建立反向关系：serie 也知道这个 acteur

    def getNom(self):
        return self.nom

    def getSerie(self):
        return self.serie
