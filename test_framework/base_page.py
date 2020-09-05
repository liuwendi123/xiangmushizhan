import logging

import yaml
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote import webelement


class BasePage:
	_driver: WebDriver = None
	_current_element:webelement = None

	def start(self):
		caps={}
		caps['platformName'] = 'Android'
		caps['deviceName'] = 'emulator-5554'
		caps['appPackage'] = 'com.xueqiu.android'
		caps['appActivity'] = '.view.WelcomeActivityAlias'
		caps['noreset'] = 'True'
		#caps['dontStopAppOnReset'] = 'True'
		#caps['skipDeviceInitialization'] = 'True'
		self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',caps)
		self._driver.implicitly_wait(20)
		return self

	def stop(self):
		self._driver.quit()


	def find(self,by):
		 self._current_element = self._driver.find_element(*by)
		 return self

	def click(self):
		self._current_element.click()
		return self

	def send_keys(self,text):
		self._current_element.send_keys(text)
		return self


	def po_run(self, po_method, **kwargs):
		#读yaml文件
		with open('page_demo.yaml') as f:
			yaml_data = yaml.safe_load(f)
			for step in yaml_data[po_method]:
				if isinstance(step,dict):
					for key in step.keys():
						if key=='id':
							locator = (By.ID,step[key])
							self.find(locator)
						elif key=='click':
							self.click()
						elif key=='send_keys':
							text = str(step[key])
							for k,v in kwargs.items():
								text=text.replace('${' + k + '}',v)
							self.send_keys(text)
							#todo:更多内容
						else:
							logging.error(f"我不知道{step}")






