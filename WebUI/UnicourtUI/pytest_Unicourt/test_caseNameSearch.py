import pytest

from pytest_Unicourt.Utilities.test_utilities import Utilities
from pytest_Unicourt.pageobjects.firstPage import firstPage
from pytest_Unicourt.pageobjects.homePage import homePage
from pytest_Unicourt.pageobjects.secondPage import secondPage


@pytest.mark.usefixtures('test_launchPage')
class TestCaseName(Utilities):
    def test_searchCase(self):

        dr = self.driver

        dr.implicitly_wait(10)

        log = self.get_logger()

        home = homePage(dr)

        home.getSearchField().send_keys(self.searchText)

        log.info("{} is entered in search field".format(self.searchText))

        dr.get_screenshot_as_file('search.png')

        home.getSearchButton().click()

        first = firstPage(dr)

        listOfCases1 = first.getCaseLabels()

        dr.get_screenshot_as_file('pageOne.png')

        noOfCases1 = len(listOfCases1)

        for i in range(1, noOfCases1):
            caseName = first.getCaseLabel(str(i)).text
            self.assertText(caseName, self.searchText)

        log.info("Case name in the search results for first page has {}".format(self.searchText))

        self.jsScrollDown(dr)

        nextLink = first.getNextLink()

        self.jsClick(dr, nextLink)

        second = secondPage(dr)

        listOfCases2 = second.getCaseLabels()

        dr.get_screenshot_as_file('pageTwo.png')

        noOfCases2 = len(listOfCases2)

        for i in range(1, noOfCases2):
            caseName = second.getCaseLabel(str(i)).text
            self.assertText(caseName, self.searchText)

        log.info("Case name in the search results for second page has {}".format(self.searchText))
