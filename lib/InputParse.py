#!/usr/bin/env python
# encoding: utf-8
import sys
sys.dont_write_bytecode = True
import argparse
from pyfiglet import Figlet
# 获取版本号,并返回版本号字符串
from setting import version

# 移除字典内没有值、或值为'()'的键
def remove_dict_none_value_key(dict_, bracket=True):
    """
    移除字典内没有值、或 值为'()'的键
    bracket 是否移除值为'()'括号的键
    """
    for key in list(dict_.keys()):
        if not dict_.get(key) or dict_.get(key) is None:
            del dict_[key]
        elif bracket and dict_.get(key) == '()':
            del dict_[key]
    return dict_

# 获取版本号,并返回版本号字符串
def get_version():
    """
    获取版本号,并返回版本号字符串
    """
    return '[*] 当前的工具版本号为: {} !!!'.format(version)


class ParserCmd(object):

    def __init__(self):
        super(ParserCmd, self).__init__()
        self.parser = self.my_parser()
        self.args = self.parser.parse_args().__dict__

    def my_parser(self):
        example = """Examples:
                          \r  python3 {shell_name} -lu http://www.baidu.com
                          \r  python3 {shell_name} -lu http://www.baidu.com -p http://127.0.0.1:8080
                          \r  
                          \r  其他控制细节参数请通过setting.py进行配置
                          \r  
                          \r  T00L Version: {version}
                          \r  
                          """

        parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,add_help=True, description=Figlet().renderText("Browser-Brute"))
        # 使 example 支持换行
        parser.epilog = example.format(shell_name=parser.prog, version=version)

        # 登录页配置参数
        parser.add_argument("-lu", "--login_url", help=r"The login address, eg: http://192.168.1.1/login.aspx",default=None)  # 指定登录地址
        parser.add_argument("-t1", "--time_1", help=r"Specifies the pause time (s) before access , eg: 1", default=1, type=float)  # 指定访问前暂停时间
        parser.add_argument("-t2", "--time_2", help=r"Specifies the pause time (s) after access , eg: 1 ", default=1, type=float)  # 指定访问后暂停时间

        parser.add_argument("-ui", "--user_id", help=r"Specify the username attribute by id", default=None)  # 指定用户名属性 id
        parser.add_argument("-un", "--user_name", help=r"Specify the username attribute by name", default=None)  # 指定用户名属性 name
        parser.add_argument("-uc", "--user_class", help=r"Specify the username attribute by class, No Spaces",default=None)  # 指定用户名属性 class
        parser.add_argument("-us", "--user_css_selector", help=r"Specify the username attribute by css selector, handle Spaces",default=None)  # CSS选择属性

        parser.add_argument("-pi", "--pass_id", help=r"Specify the password attribute by id", default=None)  # 指定密码属性 id
        parser.add_argument("-pn", "--pass_name", help=r"Specify the password attribute by name", default=None)  # 指定密码属性 name
        parser.add_argument("-pc", "--pass_class", help=r"Specify the password attribute by class, No Spaces",default=None)  # 指定密码属性 class
        parser.add_argument("-ps", "--pass_css_selector", help=r"Specify the password attribute by css selector, handle Spaces",default=None)  # CSS选择属性

        parser.add_argument("-bi", "--button_id", help=r"Specify the login button attribute by id", default=None)  # 指定登录按钮属性 id
        parser.add_argument("-bn", "--button_name", help=r"Specify the login button attribute by name", default=None)  # 指定登录按钮属性 name
        parser.add_argument("-bc", "--button_class", help=r"Specify the login button attribute by class, No Spaces", default=None)  # 指定登录按钮属性 class
        parser.add_argument("-bs", "--button_css_selector", help=r"Specify the button attribute by css selector, handle Spaces",default=None)  # CSS选择属性

        # 字典配置参数
        parser.add_argument("-ud", "--user_dict", help=r"Specify the login username dict", default='username.txt')  # 指定用户名字典
        parser.add_argument("-pd", "--pass_dict", help=r"Specify the login password dict",default='password.txt')  # 指定密码字典

        # 关键字匹配参数
        # parser.add_argument("-k", "--keyword", help="Specifies the keyword to match in the return message", default='success')  # 指定在返回报文中匹配的关键字

        # 浏览器配置参数
        parser.add_argument("-bh", "--browser_headless", 
                            help=r"Specifies the Browser browser_headless, eg: True", default=False)  # 指定是否显示浏览器界面
        parser.add_argument("-bp", "--browser_proxy",
                            help=r"Specifies the Browser Proxy IP for HTTP or HTTPS , eg: http://127.0.0.1:8080",default=None)  # 指定浏览器代理服务器地址
        parser.add_argument("-bua", "--browser_useragent",
                            help=r"Specifies the Browser UserAgent , eg: Mozilla/5.0 Version/4.0",  default=None)  # 指定浏览器User Agent头
        parser.add_argument("-bud", "--browser_user_dir",
                            help=r"Specifies the Browser User Dir , eg: D:\temp\Chrome User Data",default=None)  # 指定浏览器用户数据目录
        parser.add_argument("-bcp", "--browser_chrome_path",
                            help=r"Specifies the Browser Chrome.exe Path , eg: C:\chrome\chrome.exe",default=None)  # 指定浏览器chrome.exe路径
        parser.add_argument("-bdp", "--browser_driver_path",
                            help=r"Specifies the Browser Driver Path, eg: D:\temp\chromedriver.exe", default=None)  # 指定浏览器chromedriver.exe路径

        parser.add_argument("-v", "--version", action="version", version=get_version(), help="显示程序当前版本号")
        return parser

    @staticmethod
    def init():
        parser = ParserCmd()

        return parser.args


if __name__ == '__main__':
    args = ParserCmd().init()
    print(args)
