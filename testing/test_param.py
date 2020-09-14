import pytest


@pytest.mark.parametrize('a,b,expect', [
	(1, 1, 2),
	(0.1, 0.1, 0.2),
	(100, 200, 300),
	(0, 10, 10),
	(-1, -2, -3)
], ids=['int', 'float', 'bigint', 'zero', 'minus'])
def test_case1(a, b, expect):
	print()


# 笛卡尔积
@pytest.mark.parametrize('a', [1, 2, 3, 4])
@pytest.mark.parametrize('b', [5, 6, 7, 8, 'a', 'b'])
def test_case2(a, b):
	print(f'a= {a}, b={b}')
