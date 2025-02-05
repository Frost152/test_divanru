from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class MainPage(Base):
    url = "https://www.divan.ru/"

    def __init__(self, driver):
        super().__init__(driver)

    # Locators
    locator_main_catalog_css = "button.I0naS.EnFvW"

    # Getters
    def get_url(self):
        return self.url

    def get_wait_main_catalog(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_main_catalog_css)))

    # Actions
    def click_main_catalog(self):
        self.get_wait_main_catalog().click()

    # Methods
    def open(self):
        self.driver.get(self.url)
        self.driver.maximize_window()


class Catalog(MainPage):
    # Locators
    locator_sofa_menu_item_css = ".sOgI6"

    # Getters
    def get_wait_sofa_menu_item(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_sofa_menu_item_css)))

    # Actions
    def click_sofa_menu_item(self):
        self.get_wait_sofa_menu_item().click()

    # Methods
    def go_to_sofas(self):
        self.click_sofa_menu_item()
        self.assert_compare_text(self.get_head_page().text, "Диваны и кресла")
        print('Осуществлен переход в раздел Диваны и кресла')
