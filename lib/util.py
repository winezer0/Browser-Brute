# !/usr/bin/env python3
# _*_ coding:utf-8 _*_

# 判断列表内的字符串是否某个字符串内 # 如果列表为空,就返回default值
def list_in_str(list_=None, str_=None, default=True):
    flag = False
    if list_:
        for ele in list_:
            if ele in str_:
                flag = True
                break
    else:
        flag = default
    return flag

