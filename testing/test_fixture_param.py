import pytest


@pytest.fixture(params=[('tom', 123456), ('liuwendi', 1234567)],
                ids=['用户tom', '用户liuwendi'])
def login(request):
	return (request.param)
	print("登录")


def test_case1(login):
	print(f"username:{login[0]} ,password:{login[1]}")
	print("case1")
