Feature: Association d’un acteur principal à une série

  En tant que gestionnaire de production,
  Je veux pouvoir associer un acteur principal à une série,
  Afin de gérer les informations artistiques.

  Scenario: Associer un acteur à la série Astérix
    Given une série intitulée "Astérix" avec 4 saison(s)
    And un acteur nommé "Roger Carel"
    When j’associe l’acteur à la série
    Then le nom de l’acteur principal de la série est "Roger Carel"

  Scenario Outline: Associer un acteur à d’autres séries
    Given une série intitulée "<titre>" avec <saisons> saison(s)
    And un acteur nommé "<acteur>"
    When j’associe l’acteur à la série
    Then le nom de l’acteur principal de la série est "<acteur>"


    Examples:
    | titre            | saisons | acteur         |
    | Lupin            | 1       | Omar Sy        |
    | Dark             | 2       | Anna Müller    |
    | The four seasons | 3       | Camille Cottin |

