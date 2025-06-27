# tests/test_observateur.py

import pytest
from src.Kingdom import Prince, Princess
from src.Serie import Serie

@pytest.fixture
def setup_world():
    """Prépare la princesse, le prince et deux séries."""
    princess = Princess("Ariel")
    prince   = Prince("Eric")
    serie1   = Serie(titre="La Belle et la Bête", nb_saisons=2)
    serie2   = Serie(titre="La Petite Sirène", nb_saisons=1)
    # On donne déjà une suite à serie2
    existing_suite = Serie(titre="La Petite Sirène 2", nb_saisons=1)
    serie2.suite = existing_suite

    # On abonne les séries à l'événement "saved" de la princesse
    princess.events.subscribe("saved", serie1)
    princess.events.subscribe("saved", serie2)

    return princess, prince, serie1, serie2, existing_suite

def test_series_without_suite_gets_one(setup_world):
    """Si une série n'a pas de suite, elle doit en créer une après sauvetage."""
    princess, prince, serie1, _, _ = setup_world

    prince.savePrincess(princess)

    assert serie1.suite is not None
    assert serie1.suite.titre == "La Belle et la Bête – Suite"
   

def test_series_with_existing_suite_untouched(setup_world):
    """Une série ayant déjà une suite ne doit pas en recréer une."""
    princess, prince, _, serie2, existing_suite = setup_world

    prince.savePrincess(princess)

    assert serie2.suite is existing_suite
    assert serie2.suite.titre == "La Petite Sirène 2"



