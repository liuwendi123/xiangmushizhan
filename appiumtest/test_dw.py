import pytest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


# """
# 1.打开雪球app
# 2.点击搜索款输入框
# 3.在搜索框里面搜索"阿里巴巴"
# 4.在搜索框里选择"阿里巴巴"，然后进行点击
# 5.获取这只上香港，阿里巴巴的股价，并判断这只股价的价格>200
# """

class TestDw():
	def setup(self):
		caps = {}
		caps['platformName'] = 'Android'
		caps['platformVersion'] = '6.0'
		caps['deviceName'] = 'emulator-5554'
		caps['appPackage'] = 'com.xueqiu.android'
		caps['appActivity'] = '.view.WelcomeActivityAlias'
		caps['noReset'] = 'true'
		caps['automationName']= 'UiAutomator1'
		caps['dontStopAppOnReset'] = 'true'
		caps['skipDeviceInitialization'] = 'true'
		caps['uncodeKeyBoard'] = 'true'
		caps['reseKeyBoard'] = 'true'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', caps)
		self.driver.implicitly_wait(5)

	def teardown(self):
		self.driver.quit()

	def test_search(self):
		print("搜索测试用例")
		self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
		self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")

	def test_get_current(self):
	 self.driver.find_element_by_id("com.xueqiu.android:id/tv_search").click()
	 self.driver.find_element_by_id("com.xueqiu.android:id/search_input_text").send_keys("阿里巴巴")
	 self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text='阿里巴巴']").click()
	 current_price = self.driver.find_element_by_xpath("//*[@text='09988']/../../..//*[@resource-id='com.xueqiu.android:id/current_price']")
	 print(f"阿里香港的股价：{current_price}")
	 assert float (current_price)>200

	def test_myinfo(self):
		self.driver.find_element_by_android_uiautomator(
			'new UiSelector.resource-id("com.xueqiu.android:id/tab_icon").text("name").className("android.widget.ImageView")').click()
	# self.driver.find_element_by_android_uiautomator('new,UiSelector.textContains("账号密码登录")').click()


if __name__ == '__main()__':
	pytest.main()
