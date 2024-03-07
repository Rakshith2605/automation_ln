from selenium.webdriver.common.by import By

class LinkedInLogin:
    def __init__(self, driver):
        self.driver = driver



    def enter_username(self, username):
        user_name = self.driver.find_element(By.XPATH, '//*[@id="session_key"]')
        user_name.send_keys(username)

    def enter_password(self, password):
        paswrd = self.driver.find_element(By.XPATH, '//*[@id="session_password"]')
        paswrd.send_keys(password)

    def click_login(self):
        login = self.driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
        login.click()
