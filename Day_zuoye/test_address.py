"""
作业题二:

1.使用pytest组织测试用例
2.在测试类中定义两个测试方法：
    a.成功登录的测试方法
    b.新增地址的测试方法
3.对于之前的所实现的新增地址的测试用例，实现参数化，并且使用断言来判断每次的新增的结果
"""
import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select


class TestTp:
    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        time.sleep(2)
        self.driver.get("http://localhost/")
        self.driver.find_element_by_class_name("red").click()

    def test_login(self):
        self.driver.find_element_by_id("username").send_keys("13812345678")
        self.driver.find_element_by_id("password").send_keys("123456")
        self.driver.find_element_by_id("verify_code").send_keys("8888")
        self.driver.find_element_by_name("sbtbutton").click()
        time.sleep(2)

    @pytest.mark.parametrize(('name', 'province', 'city', 'district', 'twon', 'address', 'mobile'),
                             [('小红', '1', '2', '227', '240', '东三旗村323号2院310', '13812345678'),
                              ('小强', '3102', '3224', '3364', '3369', '倍加造村西幼儿园对面', '13812345678')])
    def test_address(self, name, province, city, district, twon, address, mobile):
        """--->1.点击顶部我的订单"""
        self.driver.find_element_by_css_selector(".top-ri-header li a[target]").click()
        time.sleep(1)
        handle = self.driver.window_handles
        self.driver.switch_to.window(handle[-1])
        """--->2.在新的窗口中点击地址管理"""
        self.driver.find_element_by_link_text("地址管理").click()
        msg = int(self.driver.find_element_by_xpath("//p/em[1]").text)
        time.sleep(1)
        """--->3.点击新增地址"""
        self.driver.find_element_by_css_selector(".co_blue").click()
        """--->4.完善地址信息,输入正确的必选项,再次保存收货地址"""
        self.driver.switch_to.frame(self.driver.find_element_by_id("layui-layer-iframe100001"))
        self.driver.find_element_by_name("consignee").click()
        self.driver.find_element_by_xpath("//tr[1]/td[2]/input").send_keys(name)
        # driver.find_element_by_name("province").click()
        select = Select(self.driver.find_element_by_id("province"))
        select.select_by_value(province)
        time.sleep(1)
        select1 = Select(self.driver.find_element_by_id("city"))
        select1.select_by_value(city)
        time.sleep(1)
        select2 = Select(self.driver.find_element_by_id("district"))
        select2.select_by_value(district)
        time.sleep(1)
        select3 = Select(self.driver.find_element_by_id("twon"))
        select3.select_by_value(twon)
        time.sleep(1)
        self.driver.find_element_by_id("address").send_keys(address)
        self.driver.find_element_by_name("mobile").send_keys(mobile)
        self.driver.find_element_by_xpath("//button/span").click()
        self.driver.refresh()
        new = int(self.driver.find_element_by_xpath("//p/em[1]").text)
        assert new == msg + 1

    def teardown_class(self):
        time.sleep(3)
        self.driver.quit()
