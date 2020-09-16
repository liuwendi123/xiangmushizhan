from test2.test.base_page import BasePage
from test2.test.market import Market

###
class Main(BasePage):
	def goto_market(self):
		self.steps("../test2/test/main.yaml")
		return Market(self._driver)