# Author: yang.yang2@dauphine.eu
@tag
Feature: Observer — Création de suite de série après sauvetage de la princesse
  En tant que princesse
  Je souhaite que mon histoire ne se termine pas après avoir été sauvée par le prince, et que les séries qui m’abonnent créent automatiquement une suite
  Afin de faire en sorte que seules les séries sans suite reçoivent une nouvelle saison quand je suis sauvée.


   
  Scenario: Une série sans suite crée une suite après que la princesse est sauvée
    Given une princesse nommée "Ariel" qui n'a pas encore été sauvée
    And un prince nommé "Eric" qui n'a pas de princesse
    And une série titrée "La Petite Sirène" sans suite enregistrée
    And la série "La Petite Sirène" est abonnée à la princesse "Ariel"
    When le prince "Eric" sauve la princesse "Ariel"
    Then la série "La Petite Sirène" devrait avoir une suite intitulée "La Petite Sirène – Suite"

  Scenario: Une série qui a déjà une suite n'en crée pas de nouvelle
    Given une princesse nommée "Ariel" qui n'a pas encore été sauvée
    And un prince nommé "Eric" qui n'a pas de princesse
    And la série "La Petite Sirène" possède déjà une suite intitulée "La Petite Sirène – Suite"
    And la série "La Petite Sirène" est abonnée à la princesse "Ariel"
    When le prince "Eric" sauve la princesse "Ariel"
    Then la série "La Petite Sirène" ne devrait pas ajouter de suite supplémentaire

  Scenario Outline: Plusieurs séries réagissent correctement
    Given une princesse nommée "<princesse>" qui n'a pas encore été sauvée
    And un prince nommé "<prince>" qui n'a pas de princesse
    And une série titrée "<serie>" sans suite enregistrée
    And la série "<serie>" est abonnée à la princesse "<princesse>"
    When le prince "<prince>" sauve la princesse "<princesse>"
    Then la série "<serie>" devrait avoir une suite intitulée "<serie> – Suite"

    Examples:
      | princesse | prince | serie               |
      | Belle     | Adam   | La Belle et la Bête |
    
