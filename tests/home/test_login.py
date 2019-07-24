from time import sleep

from selenium import webdriver
from pages.home.login_page import LoginPage
from pages.home.main_page import MainPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    # For run test from KETask
    # py.test tests\home\test_login.py --browser chrome/firefox
    # pytest --alluredir /Users/ryani/Automation/KETask/Reports

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.mp = MainPage(self.driver)

    # @pytest.mark.run(order=1)
    def test_1change_language(self):
        self.mp.clickUaLang()

        result = self.mp.verifyLangUa()

        assert result == True

    #@pytest.mark.run(order=4)
    def test_2validLogin(self):
        self.lp.login('yanishevskyy@gmail.com', 'Qwerty123')

        result = self.lp.verifyLoginSuccessful()

        assert result == True
        sleep(5)


    #@pytest.mark.run(order=2)
    def test_3search_existing(self):
        self.mp.clickSearchField()
        self.mp.Search('Xiaomi')

        result = self.mp.verifySearchSuccessful()

        assert result == True

    #@pytest.mark.run(order=3)
    def test_4search_absent(self):
        self.mp.closeSocialPopUp()
        self.mp.clickLogo()
        self.mp.Search('fksdhfgsdjhfsldh')

        result = self.mp.verifySearchEmpty()

        assert result == True

    def test_5validLogin(self):
        self.mp.clickProfile()
        self.mp.clickExit()

        Logout_result = self.mp.verifyLogOut()

        assert Logout_result == True



    # @pytest.mark.run(order=10)
    # def test_invalidLogin(self):
    #     self.driver.get(self.baseURL)
    #     self.lp.login('yanishevskyy@gmail.com', 'Qwerty123invalid')
    #
    #     sleep(5)  #TODO: Convert to wait
    #     self.driver.switch_to.default_content()
    #
    #     result = self.lp.verifyLoginFailed()
    #
    #     assert result == True
    #     self.driver.refresh()
