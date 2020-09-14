from typing import List


# 修改编码格式 创建conftest.py文件
def pytest_collection_modifyitems(
		session: "Session", config: "Config", items: List["Item"]
) -> None:
	for item in items:
		item.name = item.name.encode('utf-8').decode('unicode-escape')
		item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
