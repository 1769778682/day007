"""
作业题一:
1.使用pytest组织tpshop登录测试用例,要求如下:
    a.在类级别的fixture中打开浏览器,实现最大化,设置隐式等待
    b.在函数级别的fixture中设置跳转tpshop首页，以及点击登录超链接
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


class TestTp:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)

    def setup(self):
        time.sleep(2)
        self.driver.get("http://localhost/")
        self.driver.find_element_by_class_name("red").click()

    @pytest.mark.parametrize(('username', 'password', 'verify_code', 'msg'),
                             ([('', '123456', '8888', '用户名不能为空!'), ('13812345678', '', '8888', '密码不能为空!'),
                               ('13812345678', '123456', '', '验证码不能为空!')]))
    def test_login(self, username, password, verify_code, msg):
        self.driver.find_element_by_id("username").send_keys(username)
        self.driver.find_element_by_id("password").send_keys(password)
        self.driver.find_element_by_id("verify_code").send_keys(verify_code)
        self.driver.find_element_by_name("sbtbutton").click()
        time.sleep(2)
        massage = self.driver.find_element_by_class_name("layui-layer-content").text

        print(massage)

        assert msg == massage

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()
