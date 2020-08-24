import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from work6.page.MainPage import Main


class TestWechat:
    main = None
    driver = None



    def teardown_class(self):
        self.driver.quit()

    def test_addDepartment(self):
        """
        1、打开首页
        2、跳转通讯录页面
        3、跳转添加部门页面
        4、添加部门
        5、断言：部门名称存在新添加部门
        """

        # 从首页跳转通讯录页面
        contactPage = self.main.goto_contactPage()

        # 从通讯录页面跳转添加部门页面
        addDeptPage = contactPage.goto_addDepartment()

        # 完成添加部门操作
        deptName = "质量中心"
        addDeptPage.addDepartment(deptName)

        time.sleep(2)

        findDeptName = contactPage.find_deptByName(deptName)
        assert deptName == findDeptName

    def test_addMember(self):
        # Todo 添加成员
        pass