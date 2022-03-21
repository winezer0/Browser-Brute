
# 模拟浏览器进行登录爆破工具 -- by NOVASEC   

开发及使用细节参考:

Python实现简约的selenium登录爆破框架

https://mp.weixin.qq.com/s/qLmEp8KXmYYyGaPkLWGwAw



# 更新记录

1. 20220321 添加配置文件功能,记录命令有一些不友好。[已添加]
2. 20220321 不小心删除了整个项目,需要重新积累Star啦
   

# Todo

1. 添加css选择器,处理其他三个选择器无法匹配到空格关键字的问题

2. 考虑扩展为注入JS来进行登陆参数匹配,便于用户在浏览器调试。

3. 对接验证码识别方案。

   


# 必备

1. 你需要一个Chrome浏览器

2. 你需要一个chromedriver

   ```
   Chrome与Chromedriver版本对应表（最新）【附下载链接】_蔚蓝星辰mic的博客-CSDN博客
    https://blog.csdn.net/weixin_45532870/article/details/106327359
   ```

   



# 命令示例:

```
python3 brute-selenium.py -lu http://xxxxx/login.html --user_name suLoginname  --pass_name suDwp --button_class dlButtonId -bcp "D:\xxxx\Chrome\chrome.exe" -bdp "chromedriver\chromedriver_win32_96.0.4664.45.exe"   -ud username.txt -pd password.txt 

当前版本推荐在setting.py中配置启动参数
```





# 使用方法

```
Python3 was used !!! 应该也支持python2环境[后续可能放弃支持]

选项参数：

-h, --help            查看所有帮助

#配置浏览器访问时的属性

-bh BROWSER_HEADLESS, --browser_headless 是否显示浏览器界面, 例: True

-bp BROWSER_PROXY, --browser_proxy BROWSER_PROXY
	指定浏览器代理服务器(HTTP或HTTPS)地址,  例: http://127.0.0.1:8080
-bcp BROWSER_CHROME_PATH, --browser_chrome_path BROWSER_CHROME_PATH
	指定浏览器chrome.exe路径 ,例: C:\chrome\chrome.exe 
	默认当前目录或使用环境变量下可找到的chrome.exe 

-bdp BROWSER_DRIVER_PATH, --browser_driver_path BROWSER_DRIVER_PATH
    指定浏览器chromedriver.exe路径, 例: D:temp\chromedriver.exe 
    默认当前目录或使用环境变量下可找到的chromedriver.exe 

-bud BROWSERUSERDIR, --BrowserUserDir BROWSERUSERDIR
	指定浏览器用户数据目录 ,  例: D: emp\Chrome   User Data 

-bua BROWSER_USERAGENT, --browser_useragent BROWSER_USERAGENT
	指定浏览器 UserAgent ,  例: Mozilla/5.0  Version/4.0


-t1 TIME_1, --time_1 TIME_1
	指定访问页面前暂停时间(秒) ,  例: 1 ,默认1s
-t2 TIME_2, --time_2 TIME_2
	指定访问页面后暂停时间(秒) ,  例: 1 ,默认1s

# 指定登录URL
-lu LOGIN_URL, --login_url LOGIN_URL
	指定登录页面地址,  例: http://192.168.1.1/login.aspx



#定位登录用户名框框，三选一
-ui USER_ID, --user_id USER_ID
	指定登录用户名框属性 id值
-un USER_NAME, --user_name USER_NAME
	指定登录用户名框属性 name值
-uc USER_CLASS, --user_class USER_CLASS
	指定登录用户名框属性 class值，不能存在空格

#定位登录密码框框，三选一
-pi PASS_ID, --pass_id PASS_ID
	指定登录密码框属性 id值
-pn PASS_NAME, --pass_name PASS_NAME
	指定登录密码框属性 id值
-pc PASS_CLASS, --pass_class PASS_CLASS
	指定登录密码框属性 class值，不能存在空格

#定位登录按钮，三选一
-bi BUTTON_ID, --button_id BUTTON_ID
	指定登录按钮属性 id值
-bn BUTTON_NAME, --button_name BUTTON_NAME
	指定登录按钮属性 name值
-bc BUTTON_CLASS, --button_class BUTTON_CLASS
	指定登录按钮属性 class值，不能存在空格

#指定账号密码字典
-ud USER_DICT, --user_dict USER_DICT
	指定登录爆破用的用户名字典，默认username.txt
-pd PASS_DICT, --pass_dict PASS_DICT
	指定登录爆破用的用户名字典，默认password.txt

#指定结果匹配关键字,适用于已经知道登陆成功返回包的情况。
-k KEYWORD, --keyword KEYWORD
	指定登录爆破用的用户名字典，默认password.txt
```



