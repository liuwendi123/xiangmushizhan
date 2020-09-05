from test2.test.app import App


class TestSearch:
	def test_search(self):
		App().start().main().goto_market().goto_serach().search("jd")