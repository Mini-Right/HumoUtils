#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2021/6/29 下午7:02
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : address.py
# @Software    : PyCharm
# @Description : 生成地址
import json
import random


class GenerateAddress(object):
    area_list = json.load(
        open(f"./area.json", encoding="utf-8"))

    @classmethod
    def get_random_area(cls):
        """获取包含最细粒度的随机地区编码及地址"""
        name = ""
        province_len = len(cls.area_list)
        province = cls.area_list[random.randint(0, province_len - 1)]
        name += province.get("label")

        city_len = len(province.get("children"))
        if city_len == 0:
            card_no = province.get("value")
            return {"value": card_no, "label": name}
        else:
            city = province.get("children")[random.randint(0, city_len - 1)]
            name += city.get("label")

            county_len = len(city.get("children"))
            if county_len == 0:
                card_no = city.get("value")
                return {"value": card_no, "label": name}
            else:
                county = city.get("children")[random.randint(
                    0, county_len - 1)]
                name += county.get("label")
                street_len = len(county.get("children"))
                if street_len == 0:
                    card_no = county.get("value")
                    return {"value": card_no, "label": name}
                else:
                    street = county.get("children")[random.randint(
                        0, street_len - 1)]
                    name += street.get("label")
                    card_no = street.get("value")
                    return {"value": card_no, "label": name}

    @classmethod
    def get_random_address(cls):
        """获取随机地址"""
        return cls.get_random_area().get("label")

    @classmethod
    def get_address(cls, address_no):
        """根据身份证前6位 获取指定的最细粒度地址"""
        address = ""
        for province in cls.area_list:
            if province.get("value") == address_no[0:2]:
                address += province.get("label")
                for city in province.get("children"):
                    if city.get("value") == address_no[0:4]:
                        address += city.get("label")
                        for county in city.get("children"):
                            if county.get("value") == address_no[0:6]:
                                address += county.get("label")
                                street = county.get("children")[random.randint(0, len(county.get("children")) - 1)]
                                address += street.get("label")
        return address + cls.get_random_estate()

    @classmethod
    def get_random_estate(cls):
        """随机生成街道小区信息"""
        common_name = ["聚源", "佳福", "驿乐", "源达", "华邦", "凯撒", "同阳", "美乐", "华尔顿", "天胜",
                       "金豪", "鹏晖", "金雅", "雅盛", "菲特", "协邦", "龙桦", "麦豪", "盛达", "荣盛",
                       "格林", "汇都", "七福", "富臣", "名豪", "裕福", "元一", "宏福", "世尊", "京华",
                       "城轩", "永嘉", "诚尔", "梦泰", "富华", "尔乐", "银都", "顺生", "金角", "领立",
                       "鑫荣", "友荣", "鼎盛", "国鼎", "双屿", "富丽", "温沙", "亿凯", "鸿华", "星辉",
                       "宏达", "博亿", "乐从", "客轩", "金锐", "天都", "君悦", "赢天", "熙和", "派高",
                       "博玛", "润新", "东蒙", "利来", "国聚", "艺诺", "诚悦", "杰宏", "文华", "美特",
                       "锐恒", "泰唐", "裕通", "永新", "兴源", "金旺", "舒雅", "正阳", "荣兴", "云天",
                       "喜象", "天龙", "银马", "诚达", "鑫汉", "玛格", "中诺", "锦都", "晟丰", "凯豪",
                       "柏菲", "华龙", "伟艺", "菲斯", "金跃", "顺冠", "铭科", "洲泰", "简艺", "诺信",
                       "优嘉", "名鸿", "江恒", "蓝图", "诚栋", "家家顺", "新家园", "银地", "华瑞", "汇德",
                       "易安居", "金航", "创元", "宏轩", "兴扬", "新瑞", "融居", "捷辰", "家客多", "优置客",
                       "华瑞", "香河永成", "优享逸栈", "元诚", "凯丽", "世豫", "宜安家", "松鹤", "鑫鸿",
                       "兴海", "银兴", "阳光沙滩", "温尚居", "盈盛", "兴盛", "迅杰", "金典", "兴凯", "吉星", "东佳",
                       "安厦", "隆志达", "江山大地", "玉溪北苑", "博源", "锦裕达", "和诚", "水源丰", "境胜", "爱家立业",
                       "华杰", "盛世恒业", "泰源", "华冠", "大溪地", "天地", "信地", "三得益", "房信", "东方",
                       "派拉蒙", "深淼", "河源", "富园", "金源", "百大", "兴达", "恩宝", "玖月", "嘉锦鹏", "益民",
                       "光怡", "德信", "八达", "富中", "国正", "奥新", "安青", "巴人", "东镜", "丰泽", "丰力", "峰岩",
                       "飞扬", "伟峰", "城铭", "村田", "大富", "大商", "星渊", "信拓", "协和", "缘通", "元凌", "远志",
                       "金地", "玉鸣", "西欧", "锄禾", "创坛", "住达", "众合", "永恒", "朝河源", "馨园", "鑫诚", "颐豪",
                       "亿华", "驿鑫", "普瑞", "强锐", "福地", "长城", "神剑", "瑞贝卡", "日盛达", "瑞邦", "三盛",
                       "荣城",
                       "深化", "松鹤", "随缘", "思维", "圣田", "盛和", "天昊", "天晟", "万方", "万邦", "图腾", "泰龙",
                       "桃园", "腾飞", "天创", "开源", "奎世", "君意", "聚缘居", "鲲鹏", "蓝石", "华美", "百家兴",
                       "京御幸福", "同心", "中佳", "地球村", "居佳", "鼎盛居", "方大", "纵横", "青商", "文振", "豫建",
                       "金居", "吉星", "南洋", "天地恒", "广龙", "纬凌特", "欧佳", "天地中", "万赢", "广通达", "玉山",
                       "同富康", "恒威", "永辉"]
        suffix = ["小区", "华庭", "苑", "湾", "府", "国际公寓", "海岸", "园", "堡"]
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]

        return f"{random.choice(common_name)}{random.choice(suffix)}{random.choice(digits)}栋{random.choice(digits)}0{random.choice(digits)}号"
