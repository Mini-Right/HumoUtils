# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 18:54
# @Author  : Mini-Right
# @Email   : www@anyu.wang
# @File    : analyticBody.py
# @Software: PyCharm

"""解析响应报文"""

import ast


def analytic(body, key: str):
    """
    根据传入的key获取报文中对应的value,支持xml、json
    """
    if not isinstance(body, dict):
        try:
            body = ast.literal_eval(body)
        except:
            body = XmlToDict().main(body)

    value = get_json_value_by_key(in_json=body, target_key=key, results=[])

    if len(value) == 0:
        return ''
    else:
        return value[-1]


def get_json_value_by_key(in_json, target_key, results=[]) -> list:
    if isinstance(in_json, dict):  # 如果输入数据的格式为dict
        for key in in_json.keys():  # 循环获取key
            data = in_json[key]
            get_json_value_by_key(data, target_key, results=results)  # 回归当前key对于的value
            if key == target_key:  # 如果当前key与目标key相同就将当前key的value添加到输出列表
                results.append(data)

    elif isinstance(in_json, list) or isinstance(in_json, tuple):  # 如果输入数据格式为list或者tuple
        for data in in_json:  # 循环当前列表
            get_json_value_by_key(data, target_key, results=results)  # 回归列表的当前的元素

    return results


import xml.etree.ElementTree as ET


class XmlToDict(object):

    def main(self, xml):
        xml = ET.XML(xml)
        dict = self.set_xml_dict(xml)
        return dict

    def set_xml_dict(self, root):
        t_dict = {}
        for sub_root in list(root):
            self.xml_dict = {root.tag: ''}
            if len(list(sub_root)) <= 0:
                t_dict.update({sub_root.tag: sub_root.text})
            else:
                re_t_dict = self.recursive_xml(sub_root)
                t_dict.update({sub_root.tag: re_t_dict})
        return {root.tag: t_dict}

    def recursive_xml(self, root):
        t_dict = {}
        # 处理层级
        for sub_root in list(root):
            if len(list(sub_root)) > 0:
                re_t_dict = self.recursive_xml(sub_root)
                t_dict.update({sub_root.tag: re_t_dict})
                continue

            t_dict.update({sub_root.tag: sub_root.text})
        return t_dict
