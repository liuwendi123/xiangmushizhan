from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWebDriverWait:
	def setup(self):
	    caps={}
	    caps['platformName'] = 'Android'
	    caps['platformVersion'] = '6.0'
	    caps['deviceName'] = 'emulator-5554'
	    caps['appPackage'] = 'com.xueqiu.android'
	    caps['appActivity'] = 'com.xueqiu.android.common.MainActivity'
	    caps['noReset'] = True
	    #caps['automationName'] = 'UiAutomator1'
	    caps['dontStopAppOnReset'] = 'true'
	    caps['skipDeviceInitialization'] = True
	    caps['uncodeKeyBoard'] = 'true'
	    caps['reseKeyBoard'] = 'true'
	    self.driver = webdriver.Remote("http://localhost:4723/wd/hub",caps)
	    self.driver.implicitly_wait(5)

	def teardown(self):
		pass

	def test_wait(self):
		self.driver.find_element_by_id("com,xueqiu.android:id/tv_search").click()
		self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("alibaba")
		self.driver.find_element_by_xpath("//*[@text='阿里巴巴']").click()
		self.driver.find_element_by_xpath("//*[contains(@resource-id,'title_container')]//*[@text='股票']").click()

		locator = (MobileBy.XPATH,"//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']" )
		WebDriverWait(self.driver,10).until(expected_conditions.element_to_be_clickable(locator))
		ele =self.driver.find_element(*locator )
		print(ele.text)
		current_price =float(ele.text)
		expect_price = 170
		assert  current_price> expect_price