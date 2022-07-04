#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/12/28 14:47
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py
# @Software    : PyCharm
# @Description :
from utils.datetime_utils import get_birthday_date
from utils.generates.address import GenerateAddress
from utils.generates.card_no import GenerateCardNo
from utils.generates.mobile import GenerateMobile
from utils.generates.name import GenerateName


def generate_card(age: str = None, birthday: str = None, sex: str = None, address: str = None):
    """
    生成身份证号
    :param age:         年龄      当存在出生日期时 以出生日期为准
    :param birthday:    出生日期
    :param sex:         性别
    :param address:     地址  身份证编码前6位
    """
    birthday = birthday if birthday else get_birthday_date(age=age)
    return GenerateCardNo.card_no(birthday=birthday, sex=sex, address=address)


def generate_name():
    """
    生成姓名
    """
    return GenerateName.name()


def generate_mobile():
    """
    生成手机号
    """
    return GenerateMobile.mobile()


def generate_address(address_no: str = None):
    """
    生成地址
    :param address_no: 身份证编码前6位， 会生成符合身份证信息的地址
    """
    if address_no:
        return GenerateAddress.get_address(address_no)
    return GenerateAddress.get_random_address()


def generate_identity_info(age: str = '20Y', sex: str = None) -> dict:
    """
    生成身份信息
    :param age:     年龄
    :param sex:     性别
    :return:
    """
    card_no = generate_card(age=age, sex=sex)
    return {
        'card_no': card_no,
        'address': generate_address(card_no[0:6]),
        'name': generate_name(),
        'mobile': generate_mobile()
    }

if __name__ == '__main__':
    a = generate_identity_info()
    print(a)