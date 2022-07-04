#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/6/28 21:45
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : excel.py
# @Software    : PyCharm
# @Description :
from typing import List

import xlsxwriter


class ToExcel(object):
    def __init__(self, excel_path: str):
        self.f = xlsxwriter.Workbook(excel_path,
                                     options={
                                         'strings_to_urls': False,
                                         'default_date_format': '%Y-%m-%d %H:%M:%S'
                                     })

    def sheet(self, title: list, table_data: List[dict], sheet_name: str = 'sheet', sheet_format: list = []):
        ws = self.f.add_worksheet(sheet_name)
        for _ in sheet_format:
            ws.set_column(*_)
        count = 0
        for i in range(len(title)):
            ws.write(count, i, title[i])
        count += 1
        # 写入excel数据
        for data in table_data:
            self.__write(ws, title, count, data)
            count += 1

    def close(self):
        self.f.close()

    def __write(self, ws, title, count, data):
        num = 0
        for _title in title:
            ws.write_string(count, num,
                            str(data[_title]) if data[_title] else '')
            num += 1
