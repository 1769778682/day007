"""
作业题一:

1.使用pytest组织tpshop登录测试用例,要求如下:
    a.在类级别的setup_class中打开浏览器,实现最大化,设置隐式等待
    b.在函数级别的setup中设置跳转tpshop首页，以及点击登录超链接
    c.组织登录测试方法,要求使用参数化组织下面的测试场景:
        测试一:不输入用户名,其它正常输入,获取弹出框结果
        测试二:不输入密码，其它正常输入，获取弹出框结果
        测试三:不输入验证码，其它正常输入，获取弹出框结果
    提示:为了保障参数方法都能用,不输入的时候也要定位元素,只是send_keys()的内容为空；
    d.添加断言,判断实际获取到的结果是否和预期结果一样。
"""
import time

import pytest
from selenium import webdriver


class TestLogin:

    def setup_class(self):
        # 创建驱动对象
        self.driver = webdriver.Chrome()
        # 最大化窗口
        self.driver.maximize_window()
        # 隐式等待
        self.driver.implicitly_wait(30)

    def setup(self):
        time.sleep(2)
        # 打开网址
        self.driver.get("http://localhost/")
        # 点击登录
        self.driver.find_element_by_class_name("red").click()

    @pytest.mark.parametrize(("username", "password", "code", "expect"), (
            [("", "123456", "8888", "用户名不能为空!"), ("15800000001", "", "8888", "密码不能为空!"),
             ("15800000001", "123456", "", "验证码不能为空!")]))
    def test_login(self, username, password, code, expect):
        """
        :param username:用户名
        :param password:密码
        :param code: 验证码
        :param expect: 期望结果
        :return:
        """
        # 打印测试数据
        print("本次测试数据:username={}, password={}, code={}, expect={}".format(username, password, code, expect))
        # 输入用户名
        self.driver.find_element_by_id("username").send_keys(username)
        # 输入密码
        self.driver.find_element_by_id("password").send_keys(password)
        # 输入验证码
        self.driver.find_element_by_id("verify_code").send_keys(code)
        # 点击登录
        self.driver.find_element_by_name("sbtbutton").click()
        # 定义一个变量来存储获取错误提示信息
        time.sleep(2)
        msg = self.driver.find_element_by_class_name("layui-layer-content").text
        # 断言
        assert msg == expect

    def teardown_class(self):
        # 关闭浏览器
        self.driver.quit()
