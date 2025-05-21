"""
Steps pour : Feature « Sauver Princess »
"""

from dataclasses import dataclass
from behave import given, when, then
from kingdom import Princess, Prince


@dataclass
class PrincessStep:
    princess: Princess
    prince: Prince

    # Scenario: Flynn sauve Rapunzel avec succès
    # @given('une princesse nommée Rapunzel qui n''a pas encore été sauvée')
    @given("une princesse nommée Rapunzel qui n'a pas encore été sauvée")
    def given_princess_not_saved(self):
        self.princess = Princess("Rapunzel", False)

    @given("un prince nommé Flynn qui n'a pas de princesse")
    def given_prince_no_princess(self):
        self.prince = Prince("Flynn", None)

    @when("Flynn sauve Rapunzel")
    def when_flynn_saves_rapunzel(self):
        self.saved = self.prince.savePrincess(self.princess)

    @then("Flynn et Rapunzel sont ensemble et Rapunzel est sauvée")
    def then_flynn_and_rapunzel_together(self):
        assert self.prince.princess == self.princess
        assert self.princess.isSaved() == True

    # Scenario Outline: Un prince sans princesse sauve une princesse qui n’a pas encore été sauvée
    @given(
        "une princesse nommée {princesse} qui n'a pas encore été sauvée: {alreadySaved}"
    )
    def step_given_princess_with_status(self, princesse, alreadySaved):
        self.princess = Princess(princesse, False if alreadySaved == "False" else True)

    @given("un prince nommé {prince} et sa princesse est: {princessDuPrince}")
    def step_given_prince_with_princess(self, prince, princessDuPrince):
        self.prince = Prince(
            prince, None if princessDuPrince == "None" else Princess(princessDuPrince)
        )

    @when("le prince sauve {princesse}")
    def step_when_prince_saves_named_princess(self, princesse):
        self.prince.savePrincess(self.princess)

    @then(
        "prince et princesse devraient être ensemble et la {princesse} devrait être {saved}"
    )
    def step_then_saved_status(self, princesse, saved):
        expected = False if saved == "False" else True
        assert self.princess.isSaved() & (self.prince.princess != None) == expected
