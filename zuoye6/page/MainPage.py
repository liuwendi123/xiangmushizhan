from zuoye6.page.BasePage import BasePage
from zuoye6.page.ContactPage import ContactPage


class Main(BasePage):
	_base_url = "https://work.weixin.qq.com/wework_admin/frame"

	def goto_contactPage(self):
		# Todo 首页跳转通讯录页面
		# 继承了父类，可直接通过self.xxx调用父类类变量
		self.findById("menu_contacts").click()

		# self.driver返回给ContactPage，共用浏览器
		return ContactPage(self.driver)