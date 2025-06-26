from abc import ABC, abstractmethod


class Person(ABC):

    @abstractmethod
    def introduce(self) -> str:
        pass
