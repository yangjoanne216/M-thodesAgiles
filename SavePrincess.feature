#Author : yang.yang2@dauphine.eu
@tag
Feature: Sauver Princess
  En tant qu'un prince
  Je veux sauver ma princesse
  Afin de vivre heureux ensemble pour toujours

  Scenario Outline : Sauver la princesse qui n'est pas encore sauvée
    Given une princesse
    And je connais son <name>
    And je sais si cette princesse n'est pas <alreadySaved>
    And je n'ai pas déjà de princesse
    When je la sauve
    And elle n'est pas encore sauvée
    And je n'ai pas encore eu une princesse
    Then je devrais être le prince de la princesse
    Then la princesse devrait être sauvée
    Then je devrais vivre heureux avec la princesse pour toujours

    Examples:
      | name       | alreadySaved | 
      | "Rapunzel" | false        |
      | "Flynn"    | false        |
    
  Scenario Outline : Sauver la princesse était déjà sauvée
    Given une princesse
    And je connais son <name>
    And je sais si cette princesse <alreadySaved>
    And je sais si j'ai eu déjà une <princesse> 
    When je la sauve
    And elle est déjà sauvée
    Then elle va me refuser et dire qu'elle a eu déjà un prince (<messageErreur>)
    Then je devrais être triste
    Then je devrais vivre malheureux sans la princesse
    Then je devrais être triste
    Then je devrais vivre malheureux sans la princesse

    Examples:
      | name | alreadySaved | messageErreur 
      | "Rapunzel" | true | "Je suis désolé, mais j'ai déjà un prince." |

      | name | princesse avant sauver | princesse après sauver
      | "Flynn" | null | null |

  Scenario Outline : Sauver la princesse quand j'ai déjà eu une princesse
    Given une princesse
    And je connais son <name>
    And je sais si cette princesse <alreadySaved>
    And je sais si j'ai eu déjà une <princesse>
    When je la sauve
    And j'ai déjà eu une <princesse>
    Then elle va me refuser et me dire je suis un prince infidèle (<messageErreur>)

    Examples:
      | name | alreadySaved avant être sauvé | alreadySaved après être sauvé | messageErreur
      | "Cinderella" | false | false | "Je suis désolé, mais je ne peux pas être avec un prince infidèle." |

      | name | princesse avant sauver | princesse après sauver
      | "Flynn" | rapunzel | rapunzel |
