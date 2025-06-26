from typing import Optional
from .Person import Person

class EventManager:
    def __init__(self):
        # Stockage : { type_d'événement : [ écouteur1, écouteur2, … ] }
        self._listeners = {}

    def subscribe(self, event_type, listener):
        self._listeners.setdefault(event_type, []).append(listener)

    def unsubscribe(self, event_type, listener):
        if event_type in self._listeners:
            self._listeners[event_type].remove(listener)

    def notify(self, event_type, data):
        for listener in self._listeners.get(event_type, []):
            listener.update(data)

class Princess(Person):
    def __init__(self, name: str = "", alreadySaved: bool = False):
        self.name = name
        self.alreadySaved = alreadySaved
        self.events = EventManager()

    def isSaved(self) -> bool:
        return self.alreadySaved

    def foundPrinceAndBeHappyForever(self):
        self.alreadySaved = True
        self.events.notify("saved", self)

    def introduce(self) -> str:
        return "Je suis une pricesse, mon nom est " + self.name


class Prince(Person):
    def __init__(self, name: str = "", princess: Optional[Princess] = None):
        self.name = name
        self.princess = princess

    def isAlreadyHadPrincess(self) -> bool:
        return self.princess is not None

    def savePrincess(self, princess: Princess):
        if not self.isAlreadyHadPrincess() and not princess.isSaved():
            self.princess = princess
            princess.foundPrinceAndBeHappyForever()

    def introduce(self) -> str:
        return "Je suis un prince, mon nom est " + self.name
