# encoding: utf-8
# time: 2020/3/23 16:11

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
from pyquery import PyQuery as pq

#browser:浏览器，将浏览器设置为谷歌驱动，
# 这里需要下载谷歌对应的驱动,使用火狐浏览器安装驱动后webdriver.Firefox()
browser = webdriver.Chrome()
#转到目标网站
browser.get('http://http://www.manmanbuy.com/')
#浏览器等待10秒
wait = WebDriverWait(browser, 10)

KEY = '耳机'

def search():
    #解决加载超时出错
    try:
        #input输入框，等待加载出元素#key，#key是在搜索输入框对应的代码右击Copy,Copy selector，复制粘贴下来
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#skey'))
        )
        #submit按钮，即搜索确认按钮，#search > div > div.form > button获取方式同理
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'body > div.main-header > div > div.search > div > div.panel > form > div.sBtn > input'))
        )
        #输入框输入键，即字，输入内容为KEY
        input.send_keys(KEY)
        #确认按钮点击
        submit.click()
        #睡眠延迟2秒，避免频繁操作封IP
        sleep(2)
        #等待加载出底部页面信息，第一页,EC.text_to_be_present_in_element为判断元素上有文本信息
        ##J_bottomPage > span.p-num > a.curr，curr为页寄存器，一般高亮显示处为所在页数
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), '1')
        )
        sleep(2)
        #执行函数获取商品信息
        get_products()
        #获取商品页数
        total = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > em:nth-child(1) > b'))
        )
        #print(total)
        #返回：<selenium.webdriver.remote.webelement.WebElement (session="fdbc8d4f1162d6d947614313fe6f032a", element="c18994bb-03a7-45aa-8554-765fdc253d30")>
        # print(total.text)
        #返回：100
        return total.text
    #超时出错时，重新执行search()程序
    except TimeoutError:
        return search()

#获取商品信息
def get_products():
    ##J_goodsList > ul > li:nth-child(60)为页末最后一个商品信息，最后一个商品信息加载出来则全页商品信息全部加载出来
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#J_goodsList > ul > li:last-child'))
    )
    #获取网页源码
    html = browser.page_source
    # print(html)
    # 解析
    doc = pq(html)
    # print(doc)
    #J_goodsList .gl-warp.clearfix .gl-item为id=J_goodsList标签下class='gl-warp.clearfix'
    # 的子标签下的class='gl-item'的标签，即每页60个商品标签，有60个结果
    items = doc('#J_goodsList .gl-warp.clearfix .gl-item').items()
    #enumerate()枚举、列举、计算
    for index, i in enumerate(items):
        # print(i('.p-name.p-name-type-2 em').text())
        # print('='*30)
        # 运行结果：
            # 康师傅方便面  Express速达面馆煮面 私房红烧牛肉面*2+金牌香辣牛肉面*2   袋装
            # 泡面
            # 礼盒整箱装
            # ==============================
            # 京东超市统一 方便面 来一桶 老坛酸菜牛肉面（辣味） 12桶 整箱装
            # ==============================

        if i('.p-img a').attr('href')[0] == '/':
            ss = 'http:' + i('.p-img a').attr('href')
        else:
            ss = i('.p-img a').attr('href')
        product = {
            'index': index,
            'price': i('.p-price i').text(),
            'name': i('.p-shop a').text(),
            'commit': i('.p-commit a').text(),
            # 'img': i('.p-mig img').attr('src')
        }
        print(product)
        #运行结果：图片爬取失败
        # {'index': 0, 'price': '', 'name': '统一京东自营旗舰店', 'commit': '23万+', 'img': None}
        # {'index': 1, 'price': '', 'name': '康师傅方便面京东自营官方旗舰店', 'commit': '27万+', 'img': None}

def next_page(page_num):
    print('-------------------------------正在翻页-------------------------------')
    sleep(2)
    try:
        #由于京东页面并不是一次性加载出来，所以可以通过下拉条下拉，模拟浏览刷新未展示商品
        browser.execute_script('window.scrollTo(0, 0.8*document.body.scrollHeight)')
        sleep(1)
        #input为底部页面转换输入框
        input = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > input'))
        )
        #submit为底部页面转换跳转确定按钮
        submit = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '#J_bottomPage > span.p-skip > a'))
        )
        #清空输入框
        input.clear()
        #输入框中输入页数
        input.send_keys(page_num)
        #确认跳转
        submit.click()
        #直到加载出page_num所在页为高亮，即确认跳转成功
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#J_bottomPage > span.p-num > a.curr'), str(page_num))
        )
        sleep(1)
        #执行函数，获取跳转页面的商品信息
        get_products()
    except TimeoutError:
        return next_page(page_num)


def main():
    total = search()
    # get_products()
    #搜索商品过后便是商品搜索结果的第一页，翻页无需跳转第一页，从第二页开始
    #int(total)+1，total的值是个字符串，int()转换为数值，range()管前不管后，所以+1
    for i in range(2, int(total)+1):
        next_page(i)

if __name__ == '__main__':
    main()






