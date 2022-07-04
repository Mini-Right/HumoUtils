#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/3/31 16:42
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : pdf2img.py
# @Software    : PyCharm
# @Description :
from typing import List

import fitz  # pymupdf
from loguru import logger




def pdf2img(pdf_path: str, save_path: str, img_name: str, page_list: List[int] = None):
    """
    PDF转PNG图片
    pdf2img(
        '/Users/mini-right/Documents/firefly/eff/humoBackEnd/files/4529ec62a3aa4a6cbda15a0dfeb34870/第一个PDF.PDF',
        '/Users/mini-right/Documents/firefly/eff/humoBackEnd/files/4529ec62a3aa4a6cbda15a0dfeb34870',
        '第一个PDF',
        [1, 3]
    )
    :param pdf_path:    PDF本地路径
    :param save_path:   PDF转图片保存的路径 不带后面的/
    :param img_name:    图片名称 不带后缀
    :param page_list:   打印页码 从1开始 为空则全部打印
    :return:
    """
    logger.debug(f"PDF转图片 pdf_path: {pdf_path} save_path: {save_path} img_name: {img_name} page_list: {page_list}")
    doc = fitz.open(pdf_path)
    for pg in range(doc.pageCount):
        this_page = pg + 1
        logger.debug(f'{img_name}开始生成第{this_page}张图片')
        # 跳过不转换的页面
        if page_list and this_page not in page_list:
            # logger.debug(f'{img_name}开始生成第{this_page}张图片 -- 跳过')
            continue
        page = doc[pg]
        rotate = int(0)
        # 每个尺寸的缩放系数为8，这将为我们生成分辨率提高64倍的图像。
        zoom_x = zoom_y = 8.0
        trans = fitz.Matrix(zoom_x, zoom_y).prerotate(rotate)
        pm = page.get_pixmap(matrix=trans, alpha=False)
        png_path = f"{save_path}/{img_name}-{this_page}.PNG"
        pm.save(png_path)
        logger.debug(f'转换图片成功: {png_path}')
