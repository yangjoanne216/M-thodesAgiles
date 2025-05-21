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
    Then Flynn et Rapunzel sont ensemble et Rapunzel est sauvée

  Scenario Outline: Un prince sans princesse sauve une princesse qui n’a pas encore été sauvée
    Given une princesse nommée <princesse> qui n'a pas encore été sauvée: <alreadySaved>
    And un prince nommé <prince> et sa princesse est: <princessDuPrince>
    When le prince sauve <princesse>
    Then prince et princesse devraient être ensemble et la <princesse> devrait être <saved>

  Examples:
    | princesse  | alreadySaved | prince  |princessDuPrince | saved  |
    | Rapunzel   | False        | Flynn   |None             | True   |
    | Olive      | True         | Brutus  |None             | False  |
    | Annie      | False        | Nick    |Rapunzel         | False  |