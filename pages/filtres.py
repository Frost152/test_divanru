import time

from selenium.common import TimeoutException, ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_class import Base


class BaseFilters(Base):
    # Locators
    locator_all_filters_button_CSS = ".S5eSU"
    locator_select_filter_xpath = "//span[text()='{}']"
    locator_apply_button_css = ".rt4b5 button"
    locator_apply_text_button_css = ".cu9ho"
    locator_apply_button_wait_text_xpath = "//span[text()='Секунду...']"
    locator_apply_button_num_text_css = ".pWRim"
    locator_filter_disclosure_button_css = ".ho0uq .VCJHC"
    locator_show_all_button_xpath = "//span[text()='Показать все']"
    locator_selected_filters_css = ".xuao5"

    # Getters
    def get_all_filters_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_all_filters_button_CSS)))

    def get_select_filter(self, filter_name):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_select_filter_xpath.format(filter_name))))

    def get_apply_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_button_css)))

    def get_apply_text_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_text_button_css))).text

    def get_apply_button_wait_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, self.locator_apply_button_wait_text_xpath)))

    def get_apply_button_num_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, self.locator_apply_button_num_text_css))).text

    def get_filter_disclosure_button(self):
        return WebDriverWait(self.driver, 1).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.locator_filter_disclosure_button_css)))

    def get_show_all_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, self.locator_show_all_button_xpath)))

    def get_selected_filters_button(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, self.locator_selected_filters_css)))

    # Actions
    def click_apply_button(self):
        self.get_apply_button().click()

    def click_all_filters_button(self):
        self.get_all_filters_button().click()

    def click_select_filter(self, filter_name):
        action = ActionChains(self.driver)
        try:
            action.move_to_element(self.get_select_filter(filter_name)).perform()
            self.get_select_filter(filter_name).click()
        except ElementClickInterceptedException:
            time.sleep(1)
            action.move_to_element(self.get_select_filter(filter_name)).perform()
            self.get_apply_text_button()
            self.get_select_filter(filter_name).click()

    def click_filter_disclosure_button(self):
        action = ActionChains(self.driver)
        try:
            elements = self.get_filter_disclosure_button()
            for i in elements:
                try:
                    action.move_to_element(i).perform()
                    i.click()
                except ElementClickInterceptedException:
                    time.sleep(1)
                    action.move_to_element(i).perform()
                    i.click()
        except TimeoutException:
            pass

    def click_show_all_button(self):
        action = ActionChains(self.driver)
        try:
            elements = self.get_show_all_button()
            for i in elements:
                try:
                    action.move_to_element(i).perform()
                    i.click()
                except ElementClickInterceptedException:
                    time.sleep(1)
                    action.move_to_element(i).perform()
                    i.click()
        except TimeoutException:
            pass

    # Methods

    def open_all_filters(self):
        self.click_filter_disclosure_button()
        self.click_show_all_button()

    def selecting_multiple_filters(self, *args):
        for i in args:
            self.click_select_filter(i)
            self.get_apply_text_button()
        num = self.get_apply_button_num_text()
        print(f"Выбрано {num}")

    def enter_filters(self, *args):
        self.click_apply_button()
        print(args)
        print(tuple([i.text for i in self.get_selected_filters_button()]))
        tp = tuple([i.text for i in self.get_selected_filters_button()])
        assert args in tp or args == tp
