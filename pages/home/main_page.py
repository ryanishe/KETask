from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging
import time


class MainPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    #_search_field = "//*[@class='search-form__input ng-pristine ng-valid ng-touched']"
    _search_field = "// *[ @ name = 'search']"
    _profile = "//a[@class='header-user-link sprite-side whitelink xhr']"
    _exit = "//a[@id='profile_signout']"
    _logo = "//*[@class='logo-link responsive-img logo-link-svg']"
    _close_popup_social = "//a[@class='social-bind-tiny-close novisited']"
    _search_button = "//*[@class='button button_color_green button_size_medium search-form__submit']"
    _lang_ru = "//a[contains(text(),'RU')]"
    _lang_ua = "//a[contains(text(),'UA')]"

    def clickUaLang(self):
        self.elementClick(self._lang_ua, locatorType="XPATH")

    def clickRuLang(self):
        self.elementClick(self._lang_ru, locatorType="XPATH")

    def verifyLangUa(self):
        result = self.isElementPresent("//*[contains(text(),' Вітаємо, ')]",
                                       locatorType="xpath")
        print("Language changed to UA Successful")
        return result

    def verifyLangRu(self):
        result = self.isElementPresent("//*[contains(text(),' Здравствуйте, ')]",
                                       locatorType="xpath")
        print("Language changed to UA Successful")
        return result

    def clickSearchField(self):
        self.elementClick(self._search_field, locatorType="XPATH")

    def clickProfile(self):
        self.elementClick(self._profile, locatorType="XPATH")

    def clickExit(self):
        self.elementClick(self._exit, locatorType="XPATH")

    def clickLogo(self):
        self.elementClick(self._logo, locatorType="XPATH")

    def closeSocialPopUp(self):
        self.elementClick(self._close_popup_social, locatorType="XPATH")

    def enterSearchElement(self, search_item):
        self.sendKeys(search_item, self._search_field)

    def clickSearchButton(self):
        self.elementClick(self._search_button, locatorType="XPATH")

    def Search(self, search_item):
        self.clickSearchField()
        self.enterSearchElement(search_item)
        time.sleep(3)
        self.clickSearchButton()

    def verifySearchSuccessful(self):
        result = self.isElementPresent("//*[contains(@class,'rz-search-result-qnty')]  [contains(text(),'Знайдено')]",
                                       locatorType="xpath")
        print("Search Successful")
        return result

    def verifySearchEmpty(self):
        result = self.isElementPresent("//*[contains(@class,'search-result-title-nothing-text')]  [contains(text(),'нічого не знайдено, спробуйте змінити запит')]",
                                       locatorType="xpath")
        print("Search is empty")
        return result

    def verifyLogOut(self):
        result = self.isElementPresent("//a[contains(@class,'header-topline__user-link link-dashed')]  [contains(text(),' увійдіть в особистий кабінет ')]",
                                       locatorType="xpath")
        print("Logout Successful")
        return result
