#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/6/29 下午7:01
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : name.py
# @Software    : PyCharm
# @Description : 生成姓名
import random


class GenerateName(object):
    @classmethod
    def name_gbk(cls, length: int = 3):
        """
        生成GBK2312编码的姓名
        gbk2312 收录了六千多常用汉字。
        对字符的编码采用两个字节相组合。
        第一个字节的范围是0xB0-0xF7,
        第二个字节的范围是0xA1-0xFE。
        主要为了测试生僻字姓名使用
        :param length: 长度
        :return:
        """
        name = ""
        for i in range(length):
            head = random.randint(176, 247)
            body = random.randint(161, 254)
            val = f"{head:x} {body:x}"
            name += "".join(
                bytes.fromhex(val).decode("gb2312", errors="ignore"))

        return "闾丘" + name

    @classmethod
    def name_unicode(cls, length: int = 3):
        """
        生成unicode编码的姓名
        在unicode码中,汉字的范围是(0x4E00, 9FBF)
        unicode码中收录了2万多个汉字,包含很多生僻的繁体字
        主要为了测试生僻字姓名使用
        :param length: 长度
        :return:
        """
        names = list(chr(random.randint(19968, 40895)) for i in range(length))
        return "".join(names)

    @classmethod
    def name(cls, length: int = 3):
        """
        生成符合firefly出单规则的姓名
        :param length: 长度
        :return:
        """
        name_str = "玥歆媛茹岚颖蓓欣璇曦弦韵蓓阳春琪蕾琬柔芝欣珊碧采婧梅华薇芳彬心颖梦华颖可鑫雪正茹优妍彤心蕾华欢婷帆妍歆漫露雯菡韵歆珊娜婷露蕾春雯"
        name = list(random.choice(name_str) for i in range(length))
        return "闾丘" + "".join(name)
