from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy


# 小练习
class TestAdd():
	def setup(self):
		desired_caps = {}
		desired_caps['platformName'] = 'Android'
		#desired_caps['platformVersion'] = '6.0'
		desired_caps['deviceName'] = 'emulator-5554'
		desired_caps['appPackage'] = 'com.tencent.wework'
		desired_caps['appActivity'] = '.launch.LaunchSplashActivity'
		desired_caps['noreset'] = "true"
		# desired_caps['dontStopAppOnReset'] = 'True'
		desired_caps['skipDeviceInitialization'] = 'true'
		desired_caps['uncodeKeyBoard'] = 'true'
		desired_caps['reseKeyBoard'] = 'true'
		self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
		self.driver.implicitly_wait(5)
	def teardown(self):
		self.driver.quit()

	def test_contact(self):
		name = "追12345"
		gender = '男'
		phonenum = "13900000001"
		self.driver.find_element(MobileBy.XPATH,"//*[@text='团队']").click()
		#self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/e5o").click()
		self.driver.find_element(MobileBy.XPATH,"//*[@text='手动输入添加']").click()
		#self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cgl").click()
		#self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/cgl").send_keys(name)
	    #//*[contains(@text,'姓名')]/../android.widget.EditText -->text包含姓名的元素的父级，class=android.widget.EditText的元素
		self.driver.find_element(MobileBy.XPATH, '//*[contains(@text, "姓名")]/../android.widget.EditText').send_keys(
			name)
		self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
		if gender == '男':
			self.driver.find_element(MobileBy.XPATH, "//*[@text='男']").click()
		else:
			self.driver.find_element(MobileBy.XPATH, "//*[@text='女']").click()
		self.driver.find_element(MobileBy.ID,"com.tencent.wework:id/f9s").send_keys(phonenum)
		self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").click()
		# toast 弹框,打印当前页面的布局结构 ，xml结构，每个页面都有个toast类,class名称是android.widget.Toast
		toasttext = self.driver.find_element(MobileBy.XPATH, "//*[@class='android.widget.Toast']").text
		assert '添加成功' == toasttext


def test_deleteContact(self):
	name = "追寻12345"

	self.driver.find_element(MobileBy.XPATH, "//*[@text='通讯录']").click()
	self.driver.find_element(MobileBy.XPATH, "//*[@text='Momo']").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/hjz").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/b53").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/e_1").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/bfe").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/f9s").click()
	self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/gq7").send_keys(name)
	searchResult = self.driver.find_element(MobileBy.ID, "com.tencent.wework:id/c5m").text
	assert "无搜索结果" == searchResult