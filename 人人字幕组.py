#!/usr/bin/python
# -*- coding: UTF-8 -*-

import wx
from parse_zimuzu import parse


class MyFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, -1, "人人字幕组网站的数据", size=(400, 300))
        panel = wx.Panel(self, -1)
        # 设置普通文本
        parser = parse('http://www.zimuzu.tv/html/top/month.html')
        result = parser.start_parse()
        text = ''
        for item in result:
            text = text + ''.join(item)

        # 显示多行文本
        wx.TextCtrl(panel, -1, value=text, size=(400, 300),
                    style=wx.TE_MULTILINE | wx.TE_READONLY)


if __name__ == "__main__":
    app = wx.PySimpleApp()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()
