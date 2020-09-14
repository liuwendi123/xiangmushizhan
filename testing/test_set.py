# setup_module和 teardown_module整个模块执行前分别被调用
def setup_module():
	print("setup:模块级别的")


def teardown_module():
	print("teardown:模块级别的")


def setup_function():
	print("setup:函数级别的")


def teardown_function():
	print("teardown:函数级别")


def test_case1():
	print("函数级别")


class TestA:
	# setup_class,teardown_class 类级别的，在每个类的执行前后被调用
	def setup_class(self):
		print("setup_class:A类级别")

	def teardown_class(self):
		print("teardown_class:A类级别")

	# setup teardown 是方法级别的，在每个类里面的测试用例前后分别 被调用一次
	def setup(self):
		print("setup:测试用例前的准备")

	def teardown(self):
		print("teardown:测试用例执行后的资源释放")

	def test_a(self):
		print("test a")

	def test_b(self):
		print("test b")

	def test_c(self):
		print("test c")

	def test_d(self):
		print("test d")


class TestB:
	# setup_class,teardown_class 类级别的，在每个类的执行前后被调用
	def setup_class(self):
		print("setup_class:B类级别")

	def teardown_class(self):
		print("teardown_class:B类级别")

	# setup teardown 是方法级别的，在每个类里面的测试用例前后分别 被调用一次
	def setup(self):
		print("setup:测试用例前的准备")

	def teardown(self):
		print("teardown:测试用例执行后的资源释放")

	def test_a(self):
		print("test a")

	def test_b(self):
		print("test b")

	def test_c(self):
		print("test c")

	def test_d(self):
		print("test d")
