from behave import *


@given('the user is on the login page')
def step_impl(context):
    context.login_page.navigate_to_login_page()


# Verify the user login with valid credentials


@when('the user inserts username "<test1@test1.com>" and password "<test1>"')
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()


@when('the user clicks to access the account')
def step_impl(context):
    context.login_page.click_login_button()


@then('the user is successfully logged into the account')
def step_impl(context):
    context.login_page.login_confirmation()


# Verify the user login with invalid password


@when('the user inserts username "<test@test>" and password "<test1>"')
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()


@when('the user clicks to access the account')
def step_impl(context):
    context.login_page.click_login_button()


@then('an error message is displayed suggesting that the password is incorrect')
def step_impl(context):
    context.login_page.incorrect_password()


# Verify the user login with unregistered username


@when('the user inserts username "<test10@test10.com>" and password "<test10>"')
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()


@when('the user clicks to access the account')
def step_impl(context):
    context.login_page.click_login_button()


@then('an error message is displayed suggesting that the e-mail is unknown')
def step_impl(context):
    context.login_page.unknown_username()


# Verify the user login without providing a required field


@when('the user inserts username "<username>" and password "<password>"')
def step_impl(context):
    context.login_page.insert_username()
    context.login_page.insert_password()


@when('the user clicks to access the account')
def step_impl(context):
    context.login_page.click_login_button()


@then('a tooltip is displayed suggesting to fill in the respective field')
def step_impl(context):
    pass
    # M-am blocat aici pentru ca nu reusesc sa gasesc sursa unui tooltip in Chrome

