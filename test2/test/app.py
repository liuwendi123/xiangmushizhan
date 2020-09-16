###启动APP
import time
###
from appium import webdriver

from test2.test.base_page import BasePage
from test2.test.main import Main


class App(BasePage):
	def start(self):
		_package="com.xueqiu.android"
		_Activity=".view.WelcomeActivityAlias"
		if self._driver is None:
			desire_scap = {}
			desire_scap["platformName"] = "android"
			desire_scap["deviceName"] = "emulator-5554"
			desire_scap["appPackage"] = _package
			desire_scap["appActivity"] = _Activity
			desire_scap["autoGrantPermissions"] = True
			desire_scap["automationName"] = "UiAutomator1"
			self._driver = webdriver.Remote('http://localhost:4723/wd/hub', desire_scap)
			self._driver.implicitly_wait(5)
		else:
			self._driver.start_activity(_package,_Activity)

		return self
	def main(self):
		return Main(self._driver)
