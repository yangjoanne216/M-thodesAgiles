# features/steps/observer_steps.py
from behave import given, when, then
from src.Kingdom import Princess, Prince
from src.Serie import Serie

@given('une princesse nommée "{name}" qui n\'a pas encore été sauvée')
def step_given_princess_not_saved(context, name):
    context.princess = Princess(name, False)

@given('un prince nommé "{name}" qui n\'a pas de princesse')
def step_given_prince_no_princess(context, name):
    context.prince = Prince(name, None)

@given('une série titrée "{title}" sans suite enregistrée')
def step_given_series_without_suite(context, title):
    context.serie = Serie(titre=title, nb_saisons=1)
    context.initial_suite = None

@given('la série "{title}" est abonnée à la princesse "{princess_name}"')
def step_given_series_subscribed(context, title, princess_name):
    # s'assurer que context.princess correspond au bon nom
    if context.princess.name != princess_name:
        context.princess = Princess(princess_name, False)
    context.princess.events.subscribe("saved", context.serie)

@given('la série "{title}" possède déjà une suite intitulée "{suite_title}"')
def step_given_series_with_existing_suite(context, title, suite_title):
    # 创建主剧集
    context.serie = Serie(titre=title, nb_saisons=1)
    # 创建并设置已有续集
    existing = Serie(titre=suite_title, nb_saisons=1)
    context.serie.suite = existing
    context.initial_suite = existing.titre
    # 仍然要订阅 princess
    context.princess.events.subscribe("saved", context.serie)

@when('le prince "{prince_name}" sauve la princesse "{princess_name}"')
def step_when_prince_saves_princess(context, prince_name, princess_name):
    # 保证 prince 和 princess 在 context 中
    if context.prince.name != prince_name:
        context.prince = Prince(prince_name, None)
    if context.princess.name != princess_name:
        context.princess = Princess(princess_name, False)
    context.prince.savePrincess(context.princess)

@then('la série "{title}" devrait avoir une suite intitulée "{expected}"')
def step_then_series_has_new_suite(context, title, expected):
    assert context.serie.titre == title
    assert context.serie.suite is not None, f"La série {title} n'a pas de suite"
    assert context.serie.suite.titre == expected, (
        f"Attendu suite '{expected}', "
        f"mais obtenu '{context.serie.suite.titre}'"
    )

@then('la série "{title}" ne devrait pas ajouter de suite supplémentaire')
def step_then_series_does_not_add_suite(context, title):
    assert context.serie.titre == title
    assert context.serie.suite is not None, "La série devrait déjà avoir une suite"
    assert context.serie.suite.titre == context.initial_suite, (
        "Une nouvelle suite a été ajoutée alors que la série en possédait déjà une"
    )
