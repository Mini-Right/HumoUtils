#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/6/29 下午7:01
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : mobile.py
# @Software    : PyCharm
# @Description : 生成手机号

import random
import string


class GenerateMobile(object):
    CMCC = ["139", "138", "137", "136", "135", "134", "159", "158", "157",
            "150", "151", "152", "188", "187", "182", "183", "184", "178"]
    CUCC = ["130", "131", "132", "156", "155", "186", "185", "176"]
    CTCC = ["133", "153", "189", "180", "181", "177"]

    @classmethod
    def __splice(cls, prefix_list):
        return str(random.choice(prefix_list)) + "".join(
            random.sample(string.digits, 8))

    @classmethod
    def cmcc_mobile(cls):
        """中国移动号段手机号"""
        return cls.__splice(cls.CMCC)

    @classmethod
    def cucc_mobile(cls):
        """中国联通号段手机号"""
        return cls.__splice(cls.CUCC)

    @classmethod
    def ctcc_mobile(cls):
        """中国电信号段手机号"""
        return cls.__splice(cls.CTCC)

    @classmethod
    def mobile(cls):
        return random.choice([cls.cucc_mobile(), cls.cmcc_mobile(), cls.ctcc_mobile()])
