import pytest
import yaml

import sys

from pythoncode.calculator import Calculator

"""
文件名以：test_*.py开头
类名以：Test开头
方法名：test_开头
"""


# 读取测试数据
def get_datas():
	with open('./datas/calc.yaml', encoding='utf-8') as f:
		mydatas = yaml.safe_load(f)
		adddatas = mydatas['add']['datas']
		myids = mydatas['add']['myids']
		return [adddatas, myids]


class TestCalc:

	def setup_class(self):
		print("开始计算")
		self.calc = Calculator()

	def teardown_class(self):
		print("结束计算")

	@pytest.mark.add
	@pytest.mark.parametrize('a,b,expect', get_datas()[0], ids=get_datas()[1])
	def test_add(self, a, b, expect):
		"""
		测试相加
		:return:
		"""
		# clac = Calculator()
		result = self.calc.add(a, b)
		assert expect == result

	@pytest.mark.add
	@pytest.mark.parametrize('a,b,expect', [
		(0.3, 0.4, 0.7),
		(0.4, 0.7, 1.1)
	], ids=['整数', '456'])
	def test_add_float(self, a, b, expect):
		# clac = Calculator()
		result = round(self.calc.add(a, b), 2)
		assert expect == result

	# @pytest.mark.add
	# def test_add2(self):
	# 	# clac = Calculator()
	# 	result = self.calc.add(2,3)
	# 	assert 5 == result

	@pytest.mark.div
	def test_div(self):
		# clac  = Calculator()
		result = self.calc.div(100, 2)
		assert 50 == result

	@pytest.mark.div
	def test_div1(self):
		# clac = Calculator()
		result = self.calc.div(50, 5)
		assert 10 == result
