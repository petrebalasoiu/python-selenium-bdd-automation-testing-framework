Feature: Shopping Cart
  Background:
    Given the user is on the home page

  @T14
  Scenario: Verify if the items added individually are stored in the shopping cart
    When the user adds 3 items in the shopping cart
    When the user clicks on the shopping cart
    Then the order summary is displayed with the items and their total amount

  @T15
  Scenario: Verify if the items can be individually removed from the shopping cart
    When the user adds 3 items in the shopping cart
    When the user clicks on the shopping cart
    When the user removes each item individually
    Then the page refreshes after every item removed until the cart is empty

  @T16
  Scenario: Verify if the items in the cart are bound per user account
    When the user logs into the account
    When the user adds 3 items in the shopping cart
    When the user logs out of the account and the cart gets empty
    Then the items in the cart are restored once the same user logs back

  @T17
  Scenario: Verify if multiple items can be removed from the cart at once
    When the user adds 3 items in the shopping cart
    When the user clicks on the shopping cart
    When the user clicks to empty the whole cart
    Then all of the items are removed at once and the cart is empty