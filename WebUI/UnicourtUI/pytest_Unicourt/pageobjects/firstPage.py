from selenium.webdriver.common.by import By


class firstPage:

    def __init__(self, driver):
        self.driver = driver

    caseLabel = (By.XPATH, "//div[@class='columns is-mobile each-result']/div/section/h3")
    nextLink = (By.XPATH, "//a[@class='pagination-next page-nav  is-uppercase']")

    def getCaseLabels(self):
        return self.driver.find_elements(*self.caseLabel)

    def getCaseLabel(self, index):
        caseIndex = (By.XPATH, "//div[@class='columns is-mobile each-result'][" + index + "]/div/section/h3")
        return self.driver.find_element(*caseIndex)

    def getNextLink(self):
        return self.driver.find_element(*self.nextLink)
