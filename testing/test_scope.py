import pytest


#
# @pytest.fixture(scope='class')
# def connDB():
# 	print("连接数据库")
# 	yield
# 	print("断开数据库")
#
# class TestDemo:
# 	def test_a(self,connDB):
# 		print("testa")
#
# 	def test_b(self,connDB):
# 		print("testb")


class TestDemo:
	def test_a(self, connDB):
		print("testa")

	def test_b(self, connDB):
		print("testb")
