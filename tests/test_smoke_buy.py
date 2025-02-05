from pages.main_page import MainPage
from pages.main_page import Catalog
import pages.popups as popups


def test_buy_sofa(browser):
    driver = browser
    mp = MainPage(driver)
    modal_wrap = popups.ModalWrapper(driver)
    popup_reg = popups.RegionPopup(driver)

    mp.open()
    modal_wrap.find_and_close_modal_wrapper()
    popup_reg.find_close_region_popup()
    mp.click_main_catalog()
    modal_wrap.find_and_close_modal_wrapper()

    catalog = Catalog(driver)
    catalog.go_to_sofas()


