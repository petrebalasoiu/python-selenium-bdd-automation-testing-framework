Feature: User Registration
  Background:
    Given the user is on the registration page

  @T5
  Scenario Outline: Verify the user registration with a valid e-mail and password
    # When the user inserts a valid username and password
    When the user inserts username "<username>" and password "<password>"
    When the user ticks the terms of service checkbox
    When the user clicks to create an account
    Then the user's account is created and the user is automatically logged in
    Examples:
    | username        | password | |
    | test2@test2.com | test2    | |
    | test3@test3.com | test3    | |

  @T6
  Scenario Outline: Verify the user registration with an invalid e-mail format without containing the "@" symbol
    # When the user inserts an invalid email format without containing the "@" symbol
    When the user inserts username "<username>" and password "<password>"
    When the user ticks the terms of service checkbox
    When the user clicks to create an account
    Then a tooltip is displayed suggesting that the "@" symbol is missing
    Examples:
    | username        | password | |
    | test2.test2     | test2    | |
    | test3.test3     | test3    | |

# Bug (1): Attempting to create an account with an invalid e-mail format that contains the "@" symbol will prompt with an error message suggesting that the username field is empty | (2) and still proceeds to create the account regardless

  @T7
  Scenario Outline: Verify the user registration with an invalid e-mail format containing the "@" symbol
    # When the user inserts an invalid e-mail format which contains the "@" symbol
    When the user inserts username "<username>" and password "<password>"
    When the user ticks the terms of service checkbox
    When the user clicks to create an account
    Then an error message is displayed suggesting that the username field is empty
    Examples:
    | username        | password | |
    | test2@test2     | test2    | |
    | test3@test3     | test3    | |


  @T8
  Scenario Outline: Verify the user registration without providing a required field
    # When the user tries to register without providing either of the required fields
    When the user inserts username "<username>" and password "<password>"
    When the user ticks the terms of service checkbox
    When the user clicks to create an account
    Then a tooltip is displayed suggesting to fill in the empty field
    Examples:
    | username        | password | |
    | test2@test2.com |          | |
    |                 | test3    | |


  @T9
  Scenario Outline: Verify the registration with an existing e-mail address
    # When the user tries to register with an existing e-mail address
    When the user inserts username "<username>" and password "<password>"
    When the user ticks the terms of service checkbox
    When the user clicks to create an account
    Then an error message is displayed suggesting that the e-mail address already exists
    Examples:
    | username        | password | |
    | test@test       | test     | |
    | test1@test1     | test1    | |