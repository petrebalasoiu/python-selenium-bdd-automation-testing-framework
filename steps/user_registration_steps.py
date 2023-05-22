from behave import *


@given('the user is on the registration page')
def step_impl(context):
    pass


# Verify the user registration with a valid e-mail and password


@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    pass


@when('the user ticks the terms of service checkbox')
def step_impl(context):
    pass


@when('the user clicks to create an account')
def step_impl(context):
    pass


@then('the user\'steps account is created and the user is automatically logged in')
def step_impl(context):
    pass


# Verify the user registration with an invalid e-mail format without containing the "@" symbol

@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    pass


@when('the user ticks the terms of service checkbox')
def step_impl(context):
    pass


@when('the user clicks to create an account')
def step_impl(context):
    pass


@then('a tooltip is displayed suggesting that the "@" symbol is missing')
def step_impl(context):
    pass


# Verify the user registration with an invalid e-mail format containing the "@" symbol


@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    pass


@when('the user ticks the terms of service checkbox')
def step_impl(context):
    pass


@when('the user clicks to create an account')
def step_impl(context):
    pass


@then('an error message is displayed suggesting that the username field is empty')
def step_impl(context):
    pass


# Verify the user registration without providing a required field


@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    pass


@when('the user ticks the terms of service checkbox')
def step_impl(context):
    pass


@when('the user clicks to create an account')
def step_impl(context):
    pass


@then('a tooltip is displayed suggesting to fill in the empty field')
def step_impl(context):
    pass


# Verify the registration with an existing e-mail address


@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    pass


@when('the user ticks the terms of service checkbox')
def step_impl(context):
    pass


@when('the user clicks to create an account')
def step_impl(context):
    pass


@then('an error message is displayed suggesting that the e-mail address already exists')
def step_impl(context):
    pass

