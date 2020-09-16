import pytest


# 当一个方法上面加个 @pytest.fixture() 装饰器就变成了fixture方法
# yield 能够激活fixture teardown操作 yield相当于return
# yield 前面的操作，相当于setup操作，yield后面的操作 相当于teardown操作
# 如果需要返回值，yield 相当于 return 直接写在yield后面即可。
# autouse=True 可以应用到所有的测试用例中，不需要传人fixture的参数
# 如果需要返回数据 则需要把fixture名字传入到测试用例里面

@pytest.fixture(autouse=True)
def login():
	print("setup-- 登录")
	username = 'liuwendi'
	password = 123456
	# return [username,password]
	yield [username, password]
	print("teardown-- 登出")


def test_case1(login):
	print(f"测试用例1-需要登录  {login}")


def test_case2():
	print("测试用例2")


def test_case3(login):
	print(f"测试用例3--- 需要登录  {login}")

# @pytest.mark.usefixtures('login')
# def test_case4():
# 	print("case4")
# 	print(login)
#
