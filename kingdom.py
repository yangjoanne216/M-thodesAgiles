from dataclasses import dataclass
from typing import Optional


class Princess:
    def __init__(self, name: str = "", alreadySaved: bool = False):
        self.name = name
        self.alreadySaved = alreadySaved

    def isSaved(self) -> bool:
        return self.alreadySaved

    def foundPrinceAndBeHappyForever(self):
        self.alreadySaved = True


class Prince:
    def __init__(self, name: str = "", princess: Optional[Princess] = None):
        self.name = name
        self.princess = princess

    def isAlreadyHadPrincess(self) -> bool:
        return self.princess is not None

    def savePrincess(self, princess: Princess):
        if not self.isAlreadyHadPrincess() and not princess.isSaved():
            self.princess = princess
            princess.foundPrinceAndBeHappyForever()
