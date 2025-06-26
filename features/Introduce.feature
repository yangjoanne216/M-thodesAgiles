@tag
Feature: Introduce oneself
  As un acteur
  I want que ce soit mon personnage qui se présente à ma place 
  So that je puisse vraiment m’immerger dans le rôle et l’interpréter de la façon la plus authentique possible
  
  Scenario: Actrice Yang se présente en tant que Rapunzel quand il joue le rôle de Rapunzel
    Given une actrice nommé Yang
    And un personnage qui est une princesse nommée Rapunzel
    When Yang joue le rôle de Rapunzel
    Then Yang devrait se présenter en tant que Rapunzel

  Scenario: Actrice Yang se présente en tant qu'elle-même quand elle ne joue pas aucun rôle
    Given une actrice nommé Yang
    When Yang ne joue aucun rôle
    Then Yang devrait se présenter en tant que Yang

  Scenario Outline: Un acteur se présente en tant que personnage qu'il joue
    Given un acteur/actrice nommé <actor>
    And un personnage qui est <role> nommé <roleName>
    When <actor> joue le rôle de <roleName>
    Then <actor> devrait se présenter en tant que <roleName>, sinon il/elle se présente en tant que <actor> : <expectedIntroduction>

  Examples:
    | actor  | role     | roleName | expectedIntroduction                        |
    | Yang   | Princess | Rapunzel | Je suis une pricesse, mon nom est Rapunzel  |
    | Flynn  | Prince   | Flynn    | Je suis un prince, mon nom est Flynn        |
    | Yang   | None     | None     | Je suis un acteur, mon nom est Yang         |