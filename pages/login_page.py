import allure

class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    def open_login(self):
        with allure.step("Open login page"):
            self.driver.get("https://google.com/")


    def login(self, user, pwd):
        with allure.step(f"Login with user: {user}"):
            self.driver.find_element("id","username").send_keys(user)
            self.driver.find_element("id","password").send_keys(pwd)
            self.driver.find_element("id","login").click()
