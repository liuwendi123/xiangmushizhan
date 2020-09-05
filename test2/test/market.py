from test2.test.base_page import BasePage
from test2.test.search import Search


class Market(BasePage):
	def goto_serach(self):
		self.steps("../test2/test/market.yaml")
		return Search(self._driver)