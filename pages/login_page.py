from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    USERNAME = (By.XPATH, '//input[@placeholder="Username"]')
    PASSWORD = (By.XPATH, '//input[@placeholder="Password"]')
    LOGIN_PAGE = (By.XPATH, '//*[@id="menu-item-24"]/a')
    LOGIN_BUTTON = (By.XPATH, '//*[@value="Intra In Contul Tau"]')
    LOGIN_CONFIRMED = (By.XPATH, '//a[text()="Contul Meu"]')
    INCORRECT_PASSWORD = (By.XPATH, '//a[text()="Ai uitat parola?"]')
    UNKNOWN_USERNAME = (By.XPATH, '//strong/parent::p[@class="modal-message"]')

    def navigate_to_login_page(self):
        self.driver.get("https://www.ohvaz.ro/")
        self.driver.find_element(*self.LOGIN_PAGE).click()

    def insert_username(self, user_name='test1@test1.com'):
        username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(self.USERNAME))
        username.send_keys(user_name)

    def insert_password(self, user_password='test1'):
        password = WebDriverWait(self.driver, 20).until((EC.presence_of_element_located(self.PASSWORD)))
        password.send_keys(user_password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def login_confirmation(self):
        confirmation = self.driver.find_element(*self.LOGIN_CONFIRMED)
        assert confirmation is not None, "Login unsuccessful"

    def incorrect_password(self):
        invalid_password = self.driver.find_element(*self.INCORRECT_PASSWORD)
        assert invalid_password is not None, "Password is valid"

    def unknown_username(self):
        unknown_username = self.driver.find_element(*self.UNKNOWN_USERNAME)
        assert unknown_username is not None, "Username is valid"


