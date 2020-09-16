from typing import List

# 修改编码格式 创建conftest.py文件
import pytest


def pytest_collection_modifyitems(
		session: "Session", config: "Config", items: List["Item"]
) -> None:
	# 修改编码
	for item in items:
		item.name = item.name.encode('utf-8').decode('unicode-escape')
		item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')


# scope = session 整个session域只执行一次
@pytest.fixture(scope='session')
def connDB():
	print("连接数据库")
	yield
	print("断开数据库")
