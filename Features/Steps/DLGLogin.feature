Feature: DLG Login
  Scenario: Login to DLG with valid parameters
    Given I launch Chrome browser
    When I open DLG Homepage
    And Enter username "test@qa-experience.com" and password "Password1"
    And Click on Login button
    Then I must successfully login