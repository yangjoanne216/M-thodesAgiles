"""
Steps pour : Feature « Introduce oneself »
"""

from dataclasses import dataclass
from behave import given, when, then
from src.Acteur import Acteur
from src.Person import Person
from src.Kingdom import Princess, Prince


@dataclass
class IntroduceLogic:
    role: Person
    actor: Acteur

    # Scenario: Actrice Yang se présente en tant que Rapunzel quand il joue le rôle de Rapunzel
    @given("une actrice nommé Yang")
    def step_given_actor(self):
        self.actor = Acteur("Yang")

    @given("un personnage qui est une princesse nommée Rapunzel")
    def step_given_princess(self):
        self.role = Princess("Rapunzel")

    @when("Yang joue le rôle de Rapunzel")
    def step_when_actor_plays_princess(self):
        self.actor.setRole(self.role)

    @then("Yang devrait se présenter en tant que Rapunzel")
    def step_then_actor_introduces_as_princess(self):
        assert self.actor.introduce() == "Je suis une pricesse, mon nom est Rapunzel"

    # Scenario: Actrice Yang se présente en tant qu'elle-même quand elle ne joue pas aucun rôle
    @when("Yang ne joue aucun rôle")
    def step_when_actor_does_not_play_role(self):
        self.actor.setRole(None)

    @then("Yang devrait se présenter en tant que Yang")
    def step_then_actor_introduces_as_self(self):
        assert self.actor.introduce() == "Je suis un acteur, mon nom est Yang"

    # Scenario Outline: Un acteur se présente en tant que personnage qu'il joue
    @given("un acteur/actrice nommé {actor}")
    def step_given_actor_name_outline(self, actor):
        self.actor = Acteur(actor)

    @given("un personnage qui est {role} nommé {roleName}")
    def step_given_role_name(self, role, roleName):
        if role == "Princess":
            self.role = Princess(roleName)
        elif role == "Prince":
            self.role = Prince(roleName)
        else:
            self.role = None

    @when("{actor} joue le rôle de {roleName}")
    def step_when_actor_plays_role(self, actor, roleName):
        if self.role is not None:
            self.actor.setRole(self.role)

    @then(
        "{actor} devrait se présenter en tant que {roleName}, sinon il/elle se présente en tant que {actor} : {expectedIntroduction}"
    )
    def step_then_actor_introduces_as_role_or_self(
        self, actor, roleName, expectedIntroduction
    ):
        assert self.actor.introduce() == expectedIntroduction
