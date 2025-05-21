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
    And qui n'est pas <alreadyHadPrincess>
    When le prince la sauve
    Then <prince> et <princesse> devraient être ensemble
    And la <princesse> devrait être <saved>

    Examples:
      | princesse  | alreadySaved |  prince |alreadyHadPrincess | saved  | 
      | "Rapunzel" | false        |"Flynn"  | false             |true    |
      | "Olive"    | true         |"Brutus" | false             |false   |
      | "Annie"    | false        |"Nick"   | true              |false   |
    
