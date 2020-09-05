import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class TouchActioon():
	def setup(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'emulator-5554'
		desired_caps['appPackage'] = 'cn.kmob.screenfingermovelock'
		desired_caps['appActivity'] = 'com.samsung.ui.MainActivity'
		desired_caps['automationName'] = 'UiAutomator1'
		desired_caps['noreset'] = "true"
		# desired_caps['dontStopAppOnReset'] = 'True'
		desired_caps['skipDeviceInitialization'] = 'true'
		desired_caps['uncodeKeyBoard'] = 'true'
		desired_caps['reseKeyBoard'] = 'true'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(5)
	def teardown(self):
		self.driver.quit()

	def test_TouchAction_unlock(self):
		action =TouchAction(self.driver)
		action.press(x=243,y=395).wait(200).move_to(x=721,y=378).wait(200).move_to(x=1190,y=364).wait(200).move_to(x=1202,y=859).wait(200).move_to\
			(x=1195,y=1339).wait(200).release().perform()



