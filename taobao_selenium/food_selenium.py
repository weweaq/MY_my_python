# Created by weweaq at 2018/8/25
#  < encoding = "utf-8">
import re
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Firefox()
wait = WebDriverWait(browser, 20)


def search():
    browser.get('https://www.taobao.com')
    try:
        input_ = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "#q"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn-search"))
        )

        input_.send_keys('美食')
        submit.click()
        # raise TimeoutException(message, screen, stacktrace)
        # selenium.common.exceptions.TimeoutException: Message:

        total = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".total"))
        )
        get_info()
        return total.text
    except TimeoutException:
        return search()


def next_page(page_num):
    try:
        input_ = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, "input.input:nth-child(2)"))
        )
        submit = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "span.btn:nth-child(4)"))
        )
        input_.clear()
        input_.send_keys(page_num)
        submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.active > span:nth-child(1)"), str(page_num))
        )
        get_info()
    except TimeoutException:
        next_page(page_num)


def get_info():
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-itemlist .items .item'))    #tag 类型可以用find_all()，也可以用find()!!!!!当然也可以
        # 必须是要两个括号，因为(By.CSS_SELECTOR, '#mainsrp-itemlist .items .item')                #set（find_all的返回类型） 不可以用find与find_all方法
    )  # 这算做一个参数，如果去掉的话，会看成两个参数，就会报错，报出 typeerror
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')
    item_list = soup.find('div', id='mainsrp-itemlist')

    # list_ = item_list.find('div', class_='items')
    # print(type(item_list.div.div))
    for each in item_list.div.find_all(class_='items'):
        each_list = each.find_all(class_='ctx-box J_MouseEneterLeave J_IconMoreNew')            #find()找不到后就会返回空值 None
        for each_info in each_list:
            print(each_info.find(class_='price g_price g_price-highlight').strong.text)


        # print(type(each_list))
        # if each_list is not None:
        #     for each_info in each_list.find_all(class_='price g_price g_price-highlight'):
        #         print(each_info.strong.text)





        #find()Z返回了两个大标签，然后在find()所以只会返回两个的第一个的值
        # print(each_list.find(class_='price g_price g_price-highlight').strong.text)
        # print(each)

        # info = {
        #     'price':each_list.find(class_='price g_price g_price-highlight')
        # }
    # for each in item_list.div.div.:                                                              #这里，不可以对find_all（）的返回值进行find操作，或者find_all操作，都是不允许的
    #     print(type(each))
    # 返回的是个标签组，那么应该是进到某个标签，在单个标签下进行.XXX.XXX这样，进到其他标签
    # for each in item_list:
    #     print(each)
    #     print('\n'+'++++++++')


def main():
    total = re.search(r'\d+', search()).group()  # r'\d*'匹配不出来是为什么 # 虽然是\d提取出来的，可仍然是str类型的数据
    # for each in range(2, int(total)+1):
    #     next_page(each)


if __name__ == '__main__':
    main()
