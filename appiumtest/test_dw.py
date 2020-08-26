import pytest
from appium import webdriver

class TestDW():
	def setup(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'emulator-5554'
		desired_caps['appPackage'] = 'com.xueqiu.android'
		desired_caps['appActivity'] = '.view.WelcomeActivityAlias'
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

	def test_search(self):
		print("搜索测试用例")
		self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
		self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
	# """
	# 1.打开雪球app
	# 2.点击搜索款输入框
	# 3.在搜索框里面搜索"阿里巴巴"
	# 4.在搜索框里选择"阿里巴巴"，然后进行点击
	# 5.获取这只上香港，阿里巴巴的股价，并判断这只股价的价格>200
	# """
	#self.driver.back()
	#self.driver.back()#返回

if __name__== '__main()__':
	pytest.main()



#from appium import webdriver
desired_caps={}
desired_caps['platformName']='Android'
desired_caps['platformVersion'] ='6.0'
desired_caps['deviceName']='emulator-5554'
desired_caps['appPackage']='com.android.settings'
desired_caps['appActivity']='com.android.settings.Settings'
desired_caps['automationName']='UiAutomator1'
desired_caps['noreset'] = 'True'
desired_caps['dontStopAppOnReset'] = 'True'
desired_caps['skipDeviceInitialization'] = 'True'
driver=webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
driver.back()#返回
driver.back()#返回
driver.quit()