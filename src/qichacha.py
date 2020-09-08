#默认使用python 2.*，如果使用的是python3.*则需要对两个语句进行替换。
from selenium import webdriver
import time
import sys
import importlib

importlib.reload(sys)              #if python 2.*
# sys.setdefaultencoding('utf-8')#if python 2.*


#伪装成浏览器，防止被识破
option = webdriver.ChromeOptions()
option.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36"')
driver = webdriver.Chrome(chrome_options=option)

#打开登录页面
driver.get('https://www.qichacha.com/user_login')
#单击用户名密码登录的标签
# tag = driver.find_element_by_xpath('//*[@id="normalLogin"]')
# 单击验证码登录
tag = driver.find_element_by_xpath('//*[@id="qrcodeLogin"]')
tag.click()
#将用户名、密码注入
# driver.find_element_by_id('nameNormal').send_keys('1123113')
# driver.find_element_by_id('pwdNormal').send_keys('zxf106344')
time.sleep(10)#休眠，人工完成验证步骤，等待程序单击“登录”
#单击登录按钮
# btn = driver.find_element_by_xpath('//*[@id="user_login_normal"]/button')
# btn.click()

inc_list = ['阿里巴巴']
# inc_len = len(inc_list)
inc_len = 200

for i in range(inc_len):
    # txt = inc_list[i]
    txt = inc_list[0]
    time.sleep(1)
    
    if (i==0):
        #向搜索框注入文字
        # txt=txt.decode('utf-8')
        driver.find_element_by_id('searchkey').send_keys(txt)
        #单击搜索按钮
        srh_btn = driver.find_element_by_xpath('//*[@class="index-searchbtn"]')
        srh_btn.click()
    else:
        #向搜索框注入下一个公司地址
        # txt=txt.decode('utf-8')
        srh_btn = driver.find_element_by_xpath('//*[@id="clearSearchkey"]')
        srh_btn.click()
        driver.find_element_by_id('headerKey').send_keys(txt)
        #搜索按钮 
        srh_btn = driver.find_element_by_xpath('/html/body/header/div/form/div/div/span/button')
        srh_btn.click()

    #获取网页地址，进入
    inner = driver.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/a').get_attribute("href")
    driver.get(inner)

    #获取首个企业文本
    print(i+1)
    qylx = driver.find_element_by_xpath('/html/body/div/div/div/div/section/table/tbody/tr[5]').text
    print(qylx)
    try:
        stock_or_others = driver.find_element_by_xpath('//*[@id="search-result"]/tr[1]/td[3]/p[4]').text
        print(stock_or_others)
    except:
        pass
    #单击进入后 官网 通过href属性获得：
    inc_web = driver.find_element_by_xpath('//*[@id="company-top"]/div[2]/div[2]/div[3]/div[1]/span[3]/a').get_attribute("href")
    print("官网："+inc_web)
    print(' ')

    if (i%50 == 0):
        time.sleep(60)

driver.close()