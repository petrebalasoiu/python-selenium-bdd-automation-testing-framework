Feature: User Login
  Background:
    Given the user is on the login page

  @T10
  Scenario: Verify the user login with valid credentials
     # When the user inserts valid credentials in the username and password fields
    When the user inserts username "<test1@test1.com>" and password "<test1>"
    When the user clicks to access the account
    Then the user is successfully logged into the account

  @T11
  Scenario: Verify the user login with invalid password
    # When the user inserts a valid username but an invalid password
    When the user inserts username "<test@test>" and password "<test1>"
    When the user clicks to access the account
    Then an error message is displayed suggesting that the password is incorrect

  @T12
  Scenario: Verify the user login with unregistered username
    # When the user inserts an unregistered e-mail address and any password
    When the user inserts username "<test10@test10.com>" and password "<test10>"
    When the user clicks to access the account
    Then an error message is displayed suggesting that the e-mail is unknown

  @T13
  Scenario Outline: Verify the user login without providing a required field
    # When the user does not provide either a username nor a password
    When the user inserts username "<username>" and password "<password>"
    When the user clicks to access the account
    Then a tooltip is displayed suggesting to fill in the respective field
    Examples:
    | username      | password | |
    | test@test     |          | |
    |               | test     | |