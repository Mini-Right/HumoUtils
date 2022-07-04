#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/4/29 20:58
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
import os

import requests as requests
from tqdm import tqdm
from loguru import logger


class Down(object):

    @classmethod
    def main(cls, url: str, local_path: str, refresh: bool = False, progress: bool = False):
        """
        :param url:         目标url地址
        :param local_path:  保存本地路径
        :param refresh:     当本地文件已存在 是否刷新
        :param progress:    是否展示进度条
        :return:
        """
        logger.debug(f"开始下载 {url} 本地路径: {local_path}")
        if os.path.exists(local_path) and refresh is False:
            logger.warning(f"{local_path} 已存在 不进行刷新处理")
            return
        down = cls.down_file_progress if progress else cls.down_file
        down(url, local_path)

    @classmethod
    def down_file(cls, url, local_path):
        session = requests.session()
        response = session.request(method='get', url=url, stream=True)
        with open(local_path, "wb") as code:
            code.write(response.content)
        print(f"{local_path} 下载完成 文件大小: {len(response.content) / 1024}kb")

    @classmethod
    def down_file_progress(cls, url, local_path):
        session = requests.session()
        response = session.request(method='get', url=url, stream=True)
        total = int(response.headers.get('content-length', 0))
        with open(local_path, 'wb') as file, tqdm(
                desc=local_path,
                total=total,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=1024):
                size = file.write(data)
                bar.update(size)
