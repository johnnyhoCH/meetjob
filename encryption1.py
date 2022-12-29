# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 19:08:08 2022

@author: user
"""

"""
====加密====

個人的登入密碼不會使用明碼儲存
會加密後儲存
"""

"""
hexdigest(), hex為十六進制, 作為十六進位數據字元串值

update(pwd.encode(encoding="utf-8"))  為針對字元串進行編碼
不進行編碼會出現"TypeError"
"""

import hashlib #導入hashlib模組 主要為加密使用

def MD5_demo(pwd):
    md = hashlib.md5()  #建立一個MD5的物件
    md.update(pwd.encode(encoding='utf-8'))
    return md.hexdigest()


if __name__ == "__main__":
    password = "abcd12345"
    md5_pwd = MD5_demo(password)
    print("加密後的文字為:" + md5_pwd)