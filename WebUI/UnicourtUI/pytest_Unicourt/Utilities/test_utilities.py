import configparser
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

config = configparser.ConfigParser()
config.read('properties.ini')


class Utilities:

    searchText = 'Google'

    @staticmethod
    def assertText(fullText, partialText):
        return partialText.lower() in fullText.lower()

    def jsClick(self, driver, element):
        driver.execute_script("arguments[0].click();", element)

    def jsScrollDown(self, driver):
        driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

    def selectCountry(self, countrylist):
        for country in countrylist:
            if country.text == self.country_name:
                country.click()
                break

    def get_logger(self):
        logger_name = logging.getLogger(__name__)
        filehandler = logging.FileHandler("casename.log")
        logger_name.addHandler(filehandler)
        log_format = logging.Formatter("%(asctime)s: %(levelname)s: %(name)s: %(message)s")
        filehandler.setFormatter(log_format)
        logger_name.setLevel(logging.INFO)
        return logger_name
