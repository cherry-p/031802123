#爬取京东商品信息，包括商品url

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def get_good(name):
    try:
        driver = webdriver.Chrome()
        # 1、往京东主页发送请求
        driver.get('https://www.jd.com/')
        # 2、输入商品名称，并回车搜索
        input_tag = driver.find_element_by_id('key')
        input_tag.send_keys(name)
        input_tag.send_keys(Keys.ENTER)

        # 3、查找所有商品div
        # good_div = driver.find_element_by_id('J_goodsList')
        good_list = driver.find_elements_by_class_name('gl-item')
        n = 1
        for good in good_list:
            # 根据属性选择器查找
            # 商品链接
            good_url = good.find_element_by_css_selector(
                '.p-img a').get_attribute('href')

            return good_url
    finally:
        driver.close()



