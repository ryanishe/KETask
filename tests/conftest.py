import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from seleniumwrapper import SeleniumWrapper

from base.webdriverfactory import WebDriverFactory

@pytest.yield_fixture()
def setUp():
    print("Running method level setUp")
    yield
    print("Running method level tearDown")


@pytest.yield_fixture(scope="class")
def oneTimeSetUp(request, browser):
    print("Running one time setUp")
    wdf = WebDriverFactory(browser)
    driver = wdf.getWebDriverInstance()

    if request.cls is not None:
        request.cls.driver = driver

    yield driver
    driver.quit()
    print("Running one time tearDown")

def pytest_addoption(parser):
    parser.addoption("--browser")
    parser.addoption("--osType", help="Type of operating system")

@pytest.fixture(scope="session")
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="session")
def osType(request):
    return request.config.getoption("--osType")

@pytest.fixture(scope="function")
def screenshot_on_failure(request):
    def fin():
        driver = SeleniumWrapper().driver
        attach = driver.get_screenshot_as_png()
        if request.node.rep_setup.failed:
            # allure.attach(request.function.__name__, attach, type='PNG')
            allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
        elif request.node.rep_setup.passed:
            if request.node.rep_call.failed:
                # allure.attach(request.function.__name__, attach, type='PNG')
                allure.attach('screenshot', driver.get_screenshot_as_png(), type=AttachmentType.PNG)
    request.addfinalizer(fin)

@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = (outcome).get_result()
    if report.when == 'call':
        if not report.passed:
            feature_request = item.funcargs['request']
            driver = feature_request.instance.driver
            allure.attach(driver.get_screenshot_as_png(), name='screenshot', attachment_type=AttachmentType.PNG)