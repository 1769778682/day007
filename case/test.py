import pytest


@pytest.mark.run(order=2)
class TestDemo:
    def setup_class(self):
        print("进入首页，最大化窗口，做测试准备")

    def teardown_class(self):
        print("测试完成后，都需要关闭浏览器")

    def test_a(self):
        print("测试不输入验证码")

    def test_b(self):
        print("测试不输入密码")


if __name__ == '__main__':
    pytest.main(['-s', 'test.py'])
