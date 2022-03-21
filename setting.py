#!/usr/bin/env python
# encoding: utf-8

# 全局配置文件
import pathlib
from lib.DataType import config

# 获取setting.py脚本所在路径作为的基本路径
BASE_DIR = pathlib.Path(__file__).parent.resolve()

# 版本号配置
version = "Ver 0.1.2 2022-03-21 21:21"

# 在配置文件中配置默认目标文件等参数 比cmd输入参数优先级低 一般作为默认参数使用
# config.target = None
# config.target_file = None


#######################浏览器默认配置#######################
config.browser_chrome_path = r"chromePortable\Chrome\chrome.exe"
config.browser_driver_path = r"chromedriver\chromedriver_win32_99.0.4844.51.exe"
config.browser_proxy = None  # http://127.0.0.1：8080
config.browser_useragent = None
config.browser_user_dir = None
config.browser_headless = False
#######################登录默认配置#######################
# 登录页面配置
config.login_url = None
config.time_1 = None  # time_1
config.time_2 = None  # time_2

config.user_id = None  # user_id
config.user_name = None # user_name
config.user_class = None  # user_class class测试存在空格时,不支持 如'input_kuang_login fin fld-error'

config.pass_id = None  # pass_id
config.pass_name = "suDwp"  # pass_name
config.pass_class = None  # pass_class

config.button_id = None  # button_id
config.button_name = None  # button_name
config.button_class = None  # button_class

# 字典配置
config.user_dict = "username.txt"
config.pass_dict = "password.txt"

# 匹配关键字配置
config.keyword = None
#######################################################
