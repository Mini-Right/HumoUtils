#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/8/30 下午7:48
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : zip.py
# @Software    : PyCharm
# @Description :
import os
import zipfile

from loguru import logger


def write_all_file_to_zip(dir_path, zip_path):
    """
    :param dir_path: 要压缩的文件夹路径
    :param zip_path: 压缩后文件夹的路径 带zip
    :return:
    """
    logger.debug(f"压缩目标文件夹:{dir_path}")
    logger.debug(f"压缩目标文件夹名称:{zip_path}")
    z = zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED)
    for dir_path, dir_names, file_names in os.walk(dir_path):
        f_path = dir_path.replace(dir_path, "")  # 这一句很重要，不replace的话，就从根目录开始复制
        f_path = f_path and f_path + os.sep or ""  # 实现当前文件夹以及包含的所有文件的压缩
        for filename in file_names:
            logger.debug(f"压缩文件:{filename}")
            z.write(os.path.join(dir_path, filename), f_path + filename)
    z.close()
    logger.debug(f"压缩目标文件夹完成:{zip_path}")
    return zip_path
