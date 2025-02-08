import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture()
def browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))
    yield driver
    # При необходимости закрывать браузер, раскомментировать строку 15
    # driver.quit()
