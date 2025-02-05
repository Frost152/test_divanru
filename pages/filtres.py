from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class BaseFilters(Base):
    # Locators
    locator_all_filters_button_CSS = ".S5eSU"
    locator_in_stock_xpath = "//div[text()='В наличии' and @class='N4z8g']"
    locator_in_type_css = "#Размеры"
    locator_in_type_css = "#Цена"
    locator_in_type_css = "#Конфигурация"
    locator_in_type_css = "#Механизмтрансформации"
    locator_in_type_css = "#Материалобивки"
    locator_in_type_css = "#Легкийуходзаобивкой"
    locator_in_type_css = "#Спальноеместо"
    locator_in_type_css = "#Формаопор"
    locator_in_type_css = "#Типопор"
    locator_in_type_css = "#Бельевойящик"
    locator_in_type_css = "#Количествопосадочныхмест"
    locator_in_type_css = "#Количествоспальныхмест"
    locator_in_type_css = "#Наличиеподлокотников"
    locator_in_type_css = "#Типподлокотников"
    locator_in_type_css = "#Наполнениепосадочногоместа"
    locator_in_type_css = "#Преимущества"
    locator_in_type_css = "#Стиль"
    locator_in_type_css = "#Подушкидекоративные"
    locator_in_type_css = "#Количествоподушеквкомплекте"
    locator_in_type_css = "#Естьвшоуруме"
    locator_in_type_css = "#Подходитдляуборкироботом-пылесосом"
    locator_in_type_css = "#Подходитдляежедневногосна"


    # Getters
    def get_all_filters_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_all_filters_button_CSS)))
    # Actions
    def click_all_filters_button(self):
        self.get_all_filters_button().click()
    # Methods
