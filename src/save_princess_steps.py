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
    rescue_success: bool | None = None

    # Scenario
    @given("une princesse")

    # Scenario Outline
    @given("une {princesse: Princess} et un {prince: Prince}")
    def given_a_princess(
        self, princess: Princess = Princess(), prince: Prince = Prince()
    ):
        self.princess = princess
        self.prince = prince

    @when("le prince sauve la princesse")
    def when_the_prince_rescues_the_princess(self):
        self.prince.rescuePrincess(self.princess)

    @then("la princesse est sauvée")
    def then_the_princess_is_rescued(self):
        self.rescue_success = self.princess.isRescued()
        assert self.rescue_success, True

    # Scenario Outline
    @given("un {prince:Prince} et une {princesse:Princess} qui {is_rescued:bool}")
    def given_a_princess_with_rescue_status(
        self, prince: Prince = Prince(), princess: Princess = Princess(is_rescued=True)
    ):
        self.princess = princess
        self.prince = prince

    @when("le prince essaie de sauver la princesse")
    def when_the_prince_tries_to_rescue_the_princess(self):
        self.prince.rescuePrincess(self.princess)

    @then("la princesse n'est pas sauvée")
    def then_the_princess_is_not_rescued(self):
        self.rescue_success = self.princess.isRescued()
        assert self.rescue_success, False

    # Scenario Outline
    @given(
        "un {prince:Prince} qui a déjà une princesse et une autre {princesse:Princess}"
    )
    def given_a_prince_with_a_princess(
        self,
        prince: Prince = Prince(princess=Princess()),
        princess: Princess = Princess(),
    ):
        self.princess = princess
        self.prince = prince

    @when("le prince essaie de sauver l'autre princesse")
    def when_the_prince_tries_to_rescue_another_princess(self):
        self.prince.rescuePrincess(self.princess)

    @then("le prince ne peut pas sauver la princesse")
    def then_the_prince_cannot_rescue_the_princess(self):
        self.rescue_success = self.princess.isRescued()
        assert self.rescue_success, False
