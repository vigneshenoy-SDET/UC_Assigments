import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def test_launchPage(request):
    url = "https://unicourt.com/"

    exe_path = "E:\\Tech\\Udemy\\Python\\Selenium\\chromedriver"

    web_dr = webdriver.Chrome(executable_path=exe_path)

    web_dr.maximize_window()

    web_dr.get(url)

    request.cls.driver = web_dr

    yield

    web_dr.close()
