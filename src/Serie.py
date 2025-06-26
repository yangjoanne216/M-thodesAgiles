from dataclasses import dataclass

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
        # 如果已经是同一个续集，直接返回
        if self._suite is value:
            return

        # 清理旧关系（将旧续集断开）
        if self._suite is not None:
            self._suite = None

        # 设定新的续集
        self._suite = value

    @property
    def is_long_running(self):
        return self.nb_saisons >= 3
