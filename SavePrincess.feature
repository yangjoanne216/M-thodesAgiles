#Author : yang.yang2@dauphine.eu
@tag
Feature: Sauver Princess
  As a prince
  I want sauver ma princesse
  So that vivre heureux ensemble pour toujours

  Scenario Outline : Sauver la princesse qui n'est pas encore sauvée
    Given une <princesse>
    And qui n'est pas <alreadySaved>
    And un <prince>
    And qui n'a pas déjà de princesse
    When la prince la sauve
    Then <prince> et <princesse> devraient être ensemble
    Then la <princesse> devrait être <saved>

    Examples:
      | princesse  | alreadySaved | prince   | saved  | 
      | "Rapunzel" | false        | "Flynn"  | true   |
      | "Olive"    | true         | "Brutus" | false  |
    
  Scenario Outline : Sauver la princesse était déjà sauvée
    Given une <princesse>
    And qui est <alreadySaved>
    When la prince la sauve
    Then elle va lui refuser et dire qu'elle a eu déjà un prince (<messageErreur>)

    Examples:
      | princesse  | alreadySaved | messageErreur                               |
      | "Rapunzel" | true         | "Je suis désolé, mais j'ai déjà un prince." |

  Scenario Outline : Sauver la princesse quand la prince a déjà une princesse
    Given une princesse
    And la prince <alreadyHadPrincess>
    When la <prince> la sauve
    Then elle va lui refuser et lui dire il est un prince infidèle (<messageErreur>)

    Examples:
      | prince  | alreadyHadPrincess | messageErreur                                                       |
      | "Flynn" | true               | "Je suis désolé, mais je ne peux pas être avec un prince infidèle." |
