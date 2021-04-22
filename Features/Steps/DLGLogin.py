from behave import *
from selenium import webdriver

@given('I launch Chrome browser')
def launchBrowser(context):
    context.driver = webdriver.Chrome()

@when('I open DLG Homepage')
def openHomePage(context):
    context.driver.get("https://login.dev.qa-experience.com")


@when('Enter username "{user}" and password "{pwd}"')
def enterLoginCredentials(context, user, pwd):
    context.driver.find_element_by_name("loginUsername").send_keys(user)
    context.driver.find_element_by_name("loginPassword").send_keys(pwd)


@when('Click on Login button')
def loginButton(context):
    context.driver.find_element_by_tag_name("button").click()


@then('I must successfully login')
def loggedinSuccessfully(context):
    text = context.driver.find_element_by_xpath("//div[contains(text(),'Successfully logged in!')]").text
    assert text == 'Successfully logged in!'
    context.driver.close()
