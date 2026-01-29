Feature: Login

  Scenario: Valid Login
    Given user is on login page
    When users enter valid credential
    Then user should be on dashboard