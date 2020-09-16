# scope = session 整个session域只执行一次
import pytest


@pytest.fixture(scope='session')
def connDB():
	print("连接数据库 AAAAA")
	yield
	print("断开数据库 AAAAA")
