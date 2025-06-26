from dataclasses import dataclass
from .Kingdom import Princess

@dataclass
class Serie:
    titre: str = "Astérix"
    nb_saisons: int = 4
    _suite: 'Serie' = None
    acteur_principal: 'Acteur' = None  # ✅ 新增属性：反向关联 Acteur

    def __str__(self):
        return f"Série: {self.titre}. Elle a {self.nb_saisons} saison(s)."

    def ajouter_saison(self):
        self.nb_saisons += 1

    def set_acteur(self, acteur):
        self.acteur_principal = acteur  # ✅ 新增方法：接受 acteur 并保存为主角

    def get_acteur(self):
        return self.acteur_principal  # ✅ 可选：返回已设定的主角

    @property
    def suite(self):
        return self._suite

    @suite.setter
    def suite(self, value: 'Serie'):
        # Si c'est déjà la même suite, ne rien faire
        if self._suite is value:
            return

        # Nettoyer l'ancienne relation (dissocier la suite précédente)
        if self._suite is not None:
            self._suite = None

        # Définir la nouvelle suite
        self._suite = value

    @property
    def is_long_running(self):
        return self.nb_saisons >= 3
    
     # Rappel de l'observateur
    def update(self, subject):
        if isinstance(subject, Princess) and subject.isSaved():
           # **Ajouter la suite uniquement s'il n'existe pas déjà de suite**
            if self._suite is None:
                self.addSuite()
    
    def addSuite(self):
        new_title = f"{self.titre} – Suite"
        suite = Serie(titre=new_title, nb_saisons=1)
        self.suite = suite
        print(f"→ Création de la suite pour '{self.titre}' : '{suite.titre}'")
