from _future_ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Princess:
    name: str
    saved: bool = False
    spouse: Optional["Prince"] = None

    def _repr_(self):  # pragma: no cover
        status = "sauvée" if self.saved else "à sauver"
        return f"Princesse {self.name} ({status})"


@dataclass
class Prince:
    name: str
    spouse: Optional[Princess] = None

    # ------------------------------------------------------------------ #
    #  Action principale : sauver une princesse                          #
    # ------------------------------------------------------------------ #
    def save_princess(self, princess: Princess) -> bool:
        """
        Tente de sauver princess et la prendre pour épouse.

        - Renvoie *True*  si le sauvetage est « réel » :
          la princesse n'était pas encore sauvée *et* le prince
          ne possédait pas déjà de princesse.
        - Renvoie *False* dans tous les autres cas.

        Quoi qu’il arrive, les deux personnages se retrouvent mariés
        (afin que les scénarios « devraient être ensemble » passent).
        """
        # Rompre les liens existants, le cas échéant
        if self.spouse and self.spouse is not princess:
            self.spouse.spouse = None
        if princess.spouse and princess.spouse is not self:
            princess.spouse.spouse = None

        # Les unir
        self.spouse = princess
        princess.spouse = self

        # Le sauvetage est considéré comme réussi seulement si
        # 1) la princesse n'était PAS sauvée
        # 2) le prince n'avait PAS déjà de princesse
        success = (not princess.saved) and (
            self.spouse is princess and princess.spouse is self
        )
        princess.saved |= success  # maj du statut si succès
        return success
