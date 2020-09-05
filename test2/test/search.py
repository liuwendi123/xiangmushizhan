from test2.test.base_page import BasePage


class Search(BasePage):
	def search(self,value):
		self._params["value"]=value
		self.steps("../test2/test/search.yaml")

