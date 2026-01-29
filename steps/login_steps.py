from pytest_bdd import given, when, then
from pages.login_page import LoginPage
import allure

@given("user is on login page")
def open_page(driver):
    LoginPage(driver).open_login()

@when("user enters valid credentials")
def do_login(driver):
    LoginPage(driver).login("admin", "admin123")

@then("dashboard should be displayed")
def verify_dashboard(driver):
    with allure.step("Verify dashboard page"):
        assert "Dashboard" in driver.title
