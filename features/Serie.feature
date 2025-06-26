Feature: Gestion des saisons d'une série

  En tant que gestionnaire de séries,
  Je veux pouvoir ajouter des saisons à une série,
  Afin de suivre l’évolution de sa production.

  Scenario: Une série ajoute une saison
    Given une série intitulée "Astérix" avec 4 saison(s)
    When j’ajoute une nouvelle saison
    Then la série doit avoir 5 saison(s)

  Scenario Outline: Ajouter une saison à une série existante
    Given une série intitulée "<titre>" avec <saisons> saison(s)
    When j’ajoute une nouvelle saison
    Then la série doit avoir <attendu> saison(s)

    Examples:
      | titre            | saisons | attendu |
      | Astérix          | 4       | 5       |
      | Lupin            | 5       | 6       |
      | The four seasons | 1       | 2       |
