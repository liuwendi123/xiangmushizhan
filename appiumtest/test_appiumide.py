from appium import webdriver

from appiumtest.test_firstappium import driver

desire_scap = {
    "platformName": "android",
    "deviceName": "emulator-5554",
    "appPackage": "com.xueqiu.android",
    "appActivity": ".view.WelcomeActivityAlias",
    "automationName": "UiAutomator1",
    "noReset": True
}
import logging

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


class BasePage:
    logging.basicConfig(level=logging.INFO)

    def __init__(self, driver: WebDriver = None):
        self.driver = driver

    def find(self, locator):
        logging.info(locator)
        return self.driver.find_element(*locator)

    def find_and_click(self, locator):
        logging.info("点击")
        self.find(locator).click()

    def find_and_sendkeys(self, locator, value):
        logging.info("输入")

        self.find(locator).send_keys(value)

    def find_by_scroll_and_click(self, text):
        logging.info("滚动查找并点击")
        logging.info(text)

        element = (MobileBy.ANDROID_UIAUTOMATOR,
                   'new UiScrollable(new UiSelector()'
                   '.scrollable(true).instance(0))'
                   '.scrollIntoView(new UiSelector()'
                   f'.text("{text}").instance(0));')
        self.find(element).click()

    def get_toasttext(self):
        logging.info("获取toast")
        text = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
        logging.info(text)

        return text, desire_scap)
        driver.implicitly_wait(10)

        el1 = driver.find_element_by_id("com.xueqiu.android:id/tv_search")
        el1.click()
        el2 = driver.find_element_by_id("com.xueqiu.android:id/search_input_text")
        el2.send_keys("albabab")
