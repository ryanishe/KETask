"""
@package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.getWebDriverInstance()
"""
import traceback
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

option = Options()

option.add_argument("--disable-infobars")
option.add_argument("--window-size=1920,1080")
option.add_argument("start-maximized")
option.add_argument("--disable-extensions")
option.add_argument("no-cache")
option.add_argument("--headless")
option.add_argument("--no-sandbox")

# Pass the argument 1 to allow and 2 to block
option.add_experimental_option("prefs", {
    "profile.default_content_setting_values.notifications": 1
})

desiredCapabilities={
    "browserName":"chrome"
}
class WebDriverFactory():

    def __init__(self, browser):
        """
        Inits WebDriverFactory class

        Returns:
            None
        """
        self.browser = browser
    """
        Set chrome driver and iexplorer environment based on OS

        chromedriver = "C:/.../chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        self.driver = webdriver.Chrome(chromedriver)

        PREFERRED: Set the path on the machine where browser will be executed
    """
    """
    To run in ubuntu container
    cd "/Users/ryani/Automation/selenium_grid" && docker build -t ubuntu-desktop . && docker run -v /Users/ryani/Automation/KETask:/tmp/KETests ubuntu-desktop /bin/bash -exec "cd /tmp/KETests/tests/home/ && pytest --alluredir /tmp/KETests/Reports/ --browser ubuntu_chrome"
    """

    def getWebDriverInstance(self):
        """
       Get WebDriver Instance based on the browser configuration

        Returns:
            'WebDriver Instance'
        """
        baseURL = "https://rozetka.com.ua"
        if self.browser == "iexplorer":
            # Set Ie driver
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            # Set Chrome driver
            driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', desired_capabilities = desiredCapabilities, options=option)
        elif self.browser == "ubuntu_chrome":
            # Set Chrome driver
            driver = webdriver.Chrome(executable_path='/tmp/KETests/drivers/chromedriver75_lin', options=option)
        else:
            #driver = webdriver.Remote(command_executor='http://localhost:4446/wd/hub', desired_capabilities = desiredCapabilities, options=option)
            #driver = webdriver.Remote(command_executor='http://localhost:4446/wd/hub',desired_capabilities=desiredCapabilities)
            #driver = webdriver.Chrome(executable_path='/tmp/KETests/drivers/chromedriver75_lin', options=option)
            driver = webdriver.Chrome(options=option)
            #driver = webdriver.Firefox()
        # Setting Driver Implicit Time out for An Element
        driver.implicitly_wait(3)
        # Maximize the window
        driver.maximize_window()
        # Loading browser with App URL
        driver.get(baseURL)
        return driver