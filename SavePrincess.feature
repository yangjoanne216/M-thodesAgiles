#Author : yang.yang2@dauphine.eu
@tag
Feature: Sauver Princess
  As a prince
  I want sauver ma princesse
  So that vivre heureux ensemble pour toujours
  
  Scenario: Flynn sauve Rapunzel avec succès
    Given une princesse nommée Rapunzel qui n'a pas encore été sauvée
    And un prince nommé Flynn qui n'a pas de princesse
    When Flynn sauve Rapunzel
    Then Flynn et Rapunzel sont ensemble
    And Rapunzel est sauvée

 Scenario: Brutus sauve Olive — échec
    Given une princesse nommée Olive qui a déjà été sauvée
    And un prince nommé Brutus qui n'a pas de princesse
    When Brutus tente de sauver Olive
    Then Olive refuse d’être avec Brutus
    And Olive dit : "Je suis désolée, mais j’ai déjà un prince."

Scenario: Nick sauve Annie — échec
    Given une princesse nommée Annie qui n'a pas encore été sauvée
    And un prince nommé Nick qui a déjà une princesse
    When Nick tente de sauver Annie
    Then Annie refuse d’être avec Nick
    And Annie dit : "Je suis désolée, mais je ne peux pas être avec un prince infidèle."

  Scenario Outline : Un prince sans princesse sauve une princesse qui n’a pas encore été sauvée
    Given une <princesse>
    And qui n'est pas <alreadySaved>
    And un <prince>
    And qui n'est pas <alreadyHadPrincess>
    When le prince la sauve
    Then <prince> et <princesse> devraient être ensemble
    And la <princesse> devrait être <saved>

    Examples:
      | princesse  | alreadySaved |  prince |alreadyHadPrincess | saved  | 
      | "Rapunzel" | false        |"Flynn"  | false             |true    |
      

  Scenario Outline : Sauver la princesse était déjà sauvée
    Given une <princesse>
    And qui est <alreadySaved>
    When la prince la sauve
    Then elle va lui refuser et dire qu'elle a eu déjà un prince (<messageErreur>)

    Examples:
      | princesse  | alreadySaved | messageErreur                               |
      | "Olive"    | true         | "Je suis désolé, mais j'ai déjà un prince." |

  Scenario Outline : Sauver la princesse quand la prince a déjà une princesse
    Given une princesse
    And la prince <alreadyHadPrincess>
    When la <prince> la sauve
    Then elle va lui refuser et lui dire il est un prince infidèle (<messageErreur>)

    Examples:
      | prince  | alreadyHadPrincess | messageErreur                                                       |
      | "Nick"  | true               | "Je suis désolé, mais je ne peux pas être avec un prince infidèle." |
    
