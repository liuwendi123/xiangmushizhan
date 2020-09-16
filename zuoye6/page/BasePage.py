"""
BasePage:页面类，供其他页面继承
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage:
	#浏览器驱动
	_base_url = ""

	def __init__(self, driver: WebDriver = None):  # 初始化一个方法 可以动态识别代码
		self._driver.implicitly_wait(5)
		if driver is None:
			self._driver = webdriver.Chrome()
		else:
			self._driver = driver
		if self._base_url != "":
			self._driver.get(self._base_url)

	def findByClass(self, classSelector):
		classEle = self._driver.find_element(By.CSS_SELECTOR, classSelector)
		return classEle

	def findElementsByClass(self, classSelector):
		classEles = self._driver.find_elements(By.CSS_SELECTOR, classSelector)
		return classEles

	def findById(self, idSelector):
		idEle = self._driver.find_element(By.ID, idSelector)
		return idEle

	# 性能优化
	def find(self, by, locater):
		return self._driver.find_element(by, locater)