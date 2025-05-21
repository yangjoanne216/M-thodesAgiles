"""
Steps pour : Feature « Sauver Princess »
"""

from dataclasses import dataclass
from behave import given, when, then
from src.kingdom import Prince, Princess


@dataclass
class SavePrincessSteps:
    princess: Princess | None = None
    prince: Prince | None = None
    saved: bool | None = None

    # Scenario
    @given("une princesse")

    # Scenario Outline
    @given(
        "une {princesse} qui n'est pas {alreadySaved}"
        "et un {prince} et {princessDuPrince} n'est personne"
    )
    def given_a_princess(
        self,
        princess,
        prince,
        alreadySaved: bool = False,
        princessDuPrince: Princess = None,
    ):
        self.princess = Princess(princess, alreadySaved)
        self.prince = Prince(prince, princessDuPrince)

    @when("le prince la sauve")
    def when_the_prince_rescues_the_princess(self):
        self.prince.savePrincess(self.princess)

    @then(
        "{prince} et {princesse} devraient être ensemble"
        "et la {princesse} devrait être {saved}"
    )
    def then_the_princess_is_rescued(self):
        self.saved = self.princess.isSaved() & self.prince.isAlreadyHadPrincess()
        assert self.saved, True

    # Scenario Outline
    @given("une {princesse} qui est {alreadySaved}")
    def given_a_princess_with_rescue_status(self, princess, alreadySaved: bool = True):
        self.princess = Princess(princess, alreadySaved)
        self.prince = Prince()

    @when("la prince la sauve")
    def when_the_prince_tries_to_rescue_the_princess(self):
        self.prince.savePrincess(self.princess)

    @then(
        "{prince} et {princesse} ne pourraient pas être ensemble"
        "et la {princesse} ne pourraient pas être être {saved}"
    )
    def then_the_princess_is_not_rescued(self):
        self.saved = self.princess.isSaved() & self.prince.isAlreadyHadPrincess()
        assert self.saved, False

    # Scenario Outline
    @given("une princesse et un {prince} et {princessDuPrince} est déjà quelqu'un")
    def given_a_prince_with_a_princess(
        self,
        prince,
        princessDuPrince: Princess = Princess(),
    ):
        self.princess = Princess()
        self.prince = Prince(prince, princessDuPrince)

    @when("le {prince} la sauve")
    def when_the_prince_tries_to_rescue_another_princess(self):
        self.prince.savePrincess(self.princess)

    @then(
        "{prince} et {princesse} ne pourraient pas être ensemble"
        "et la {princesse} ne pourraient pas être être {saved}"
    )
    def then_the_prince_cannot_rescue_the_princess(self):
        self.saved = self.princess.isSaved() & self.prince.isAlreadyHadPrincess()
        assert self.saved, False
