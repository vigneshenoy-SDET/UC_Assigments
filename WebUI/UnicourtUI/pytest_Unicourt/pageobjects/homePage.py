from selenium.webdriver.common.by import By


class homePage:

    def __init__(self, driver):
        self.driver = driver

    searchField = (By.CSS_SELECTOR, "input#query")
    searchButton = (By.XPATH, "//button[@aria-label='search']")

    def getSearchField(self):
        return self.driver.find_element(*self.searchField)

    def getSearchButton(self):
        return self.driver.find_element(*self.searchButton)
