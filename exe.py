# -*- coding: utf-8 -*-


import os
def open_app(app_dir):
    os.startfile(app_dir)


if __name__ == "__main__":
  app_dir = r"E:\Program Files (x86)\Tencent\WeChat\WeChat.exe"
  open_app(app_dir)


