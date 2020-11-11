from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pyquery import PyQuery as pq
# browser = webdriver.Chrome()
# # #转到目标网站
# # browser.get('https://www.miaomiaozhe.com/')
# #浏览器等待10秒
# wait = WebDriverWait(browser, 10)
# KEY = '耳机'
def search():
    #解决加载超时出错
    try:
        #input输入框，等待加载出元素#key，#key是在搜索输入框对应的代码右击Copy,Copy selector，复制粘贴下来
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#hd > div > div.pricelive-search > input.pricelive-ipt'))
        )
        #submit按钮，即搜索确认按钮，#search > div > div.form > button获取方式同理
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#hd > div > div.pricelive-search > input.pricelive-sub.icon'))
        )
        #输入框输入键，即字，输入内容为KEY
        input.send_keys(KEY)
        #确认按钮点击
        submit.click()
        #睡眠延迟2秒，避免频繁操作封IP
        sleep(2)
        return
        #等待加载出底部页面信息，第一页,EC.text_to_be_present_in_element为判断元素上有文本信息
        ##J_bottomPage > span.p-num > a.curr，curr为页寄存器，一般高亮显示处为所在页数
        # wait.until(
        #     EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), '1')
        # )
        # sleep(2)
        # #执行函数获取商品信息
        # get_products()
        # #获取商品页数
        # total = wait.until(
        #     EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b'))
        # )
        #print(total)
        #返回：<selenium.webdriver.remote.webelement.WebElement (session="fdbc8d4f1162d6d947614313fe6f032a", element="c18994bb-03a7-45aa-8554-765fdc253d30")>
        # print(total.text)
        #返回：100
        # return total.text
    #超时出错时，重新执行search()程序
    except TimeoutError:
        return search()
def get_good(driver):
    # 通过JS控制滚轮滑动获取所有商品信息
    # js_code = '''
    #                                     window.scrollTo(0,100000);
    #                                 '''
    # driver.execute_script(js_code)  # 执行js代码
    # 等待数据加载
    driver.execute_script('window.scrollTo(0, 1*document.body.scrollHeight)')
    wait.until(EC.presence_of_element_located((By.CLASS_NAME,"item.cl")))
    # 商品详情wrap
    good_list = driver.find_elements_by_class_name('item.cl')
    print(good_list)
    for good in good_list:
    # 商品名称
        goods_name = good.find_element_by_class_name('title').text.replace("\n", " ")
    # 商品价格
        #goods_price = good.find_element_by_class_name('price').text.replace("\n", " ")
        print(goods_name)
    # # 评价信息
    # evaluation_btn = goods_detail.find_element_by_id('detail').find_element_by_class_name('tab-main').find_elements_by_tag_name('li')[4]
    # evaluation_btn.click()
    # print(evaluation_btn.text)
    time.sleep(10)
    # # 好评度
    # percent_con = goods_detail.find_element_by_class_name('percent-con').text.replace("\n", " ")
    # # 评价tag
    # evaluation_tags = goods_detail.find_elements_by_class_name('tag-1')
    # tags = []
    # for tag in evaluation_tags:
    #     tags.append(tag.text)
def main():
    search()
    while(1):
        get_good(driver)

if __name__ == '__main__':
    # browser = webdriver.Chrome()
    # #转到目标网站
    # browser.get('https://www.miaomiaozhe.com/')
    # #浏览器等待10秒
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    url = 'https://www.miaomiaozhe.com/'
    driver.get(url)
    wait = WebDriverWait(driver, 100)
    KEY = '耳机'
    main()
    driver.close();