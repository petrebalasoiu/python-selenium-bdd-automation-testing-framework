from behave import *


@given('the user is on the home page')
def step_impl(context):
    pass


# Verify if the items added individually are stored in the shopping cart

# @when('the user adds 3 items in the shopping cart')
# def step_impl(context):
#     pass


# @when('the user clicks on the shopping cart')
# def step_impl(context):
#     pass


@then('the order summary is displayed with the items and their total amount')
def step_impl(context):
    pass


# Verify if the items can be individually removed from the shopping cart

# @when('the user adds 3 items in the shopping cart')
# def step_impl(context):
#     pass


@when('the user clicks on the shopping cart')
def step_impl(context):
    pass


@when('the user removes each item individually')
def step_impl(context):
    pass


@then('the page refreshes after every item removed until the cart is empty')
def step_impl(context):
    pass


# Verify if the items in the cart are bound per user account

@when('the user logs into the account')
def step_impl(context):
    pass


# @when('the user adds 3 items in the shopping cart')
# def step_impl(context):
#     pass


@when('the user logs out of the account and the cart gets empty')
def step_impl(context):
    pass


@then('the items in the cart are restored once the same user logs back')
def step_impl(context):
    pass


# Verify if multiple items can be removed from the cart at once

@when('the user adds 3 items in the shopping cart')
def step_impl(context):
    pass


@when('the user clicks on the shopping cart')
def step_impl(context):
    pass


@when('the user clicks to empty the whole cart')
def step_impl(context):
    pass


@then('all of the items are removed at once and the cart is empty')
def step_impl(context):
    pass

