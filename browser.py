from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser():
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())

    def close_browser(self):
        self.driver.quit()