#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time        : 2022/4/29 18:07
# @Author      : Mini-Right
# @Email       : www@anyu.wang
# @File        : __init__.py.py
# @Software    : PyCharm
# @Description :
import datetime
import time
from typing import Dict, Optional

import arrow


def get_current_millisecond_time() -> int:
    """
    description:  获取当前时间戳-毫秒级
    :return:      1599805496610 -> str
    """
    return int(arrow.now().timestamp() * 1000)


def get_current_second_time() -> int:
    """
    description:  获取当前时间戳-秒级
    :return:
    """
    return int(arrow.now().timestamp())


def get_current_date() -> str:
    """
    description:  获取当前日期
    :return:      2021-02-19 -> str
    """
    return arrow.now().format('YYYY-MM-DD')


def get_current_time():
    """
    description:  获取当前时间
    :return:      14:41:15 -> str
    """
    return arrow.now().format('HH:mm:ss')


def get_current_datetime():
    """
    description:  获取当前日期时间
    :return:      2021-02-19 14:41:15 -> str
    """
    return arrow.now().format('YYYY-MM-DD HH:mm:ss')


def get_current_week_day() -> str:
    """
    description:  获取当前是周几
    :return:
    """
    return int(arrow.now().weekday()) + 1


def get_last_week_start_date() -> str:
    """
    description:  获取上周一日期
    :return:
    """
    return arrow.now().shift(weeks=-1, days=-get_current_week_day() + 1).format('YYYY-MM-DD')


def get_last_week_end_date() -> str:
    """
    description:  获取上周末日期
    :return:
    """
    return arrow.now().shift(weeks=-1, days=-get_current_week_day() + 1 + 6).format('YYYY-MM-DD')


def get_birthday_date(age: str, date_time: str = get_current_date()):
    """
    description:        根据年龄获取出生日期
    支持年龄类型:         18Y 18Y-1D 18Y+1M
    :param date_time:   日期
    :param age:         年龄
    :return:
    """
    age = str(age)
    if 'Y' not in age and 'M' not in age and 'D' not in age:
        age = f"{age}Y"
    shift_dict = conduct_add_subtract_shift(age)
    # 年龄倒计算 shift取反
    shift = {k: -v for k, v in shift_dict.items()}
    birthday = get_any_datetime(date_time=date_time,
                                format="YYYY-MM-DD",
                                **shift).split(" ")[0]
    return birthday


def get_any_datetime(
        date_time: Optional[str] = get_current_datetime(),
        year: Optional[int] = 0,
        month: Optional[int] = 0,
        day: Optional[int] = 0,
        hour: Optional[int] = 0,
        minute: Optional[int] = 0,
        second: Optional[int] = 0,
        format: str = "YYYY-MM-DD HH:mm:ss",
) -> str:
    """
    description:  获取距离传入日期的任意偏移时间的日期时间
    :param date_time:   时间
    :param year:        年 1代表传入时间+1年   -1代表当前时间-1年     默认=0
    :param month:       月 1代表传入时间+1月   -1代表当前时间-1月     默认=0
    :param day:         日 1代表传入时间+1日   -1代表当前时间-1日     默认=0
    :param hour:        时 1代表传入时间+1时   -1代表当前时间-1时     默认=0
    :param minute:      分 1代表传入时间+1分   -1代表当前时间-1分     默认=0
    :param second:      秒 1代表传入时间+1秒   -1代表当前时间-1秒     默认=0
    :param format:      格式
    :return:            2020-09-11 14:21:36 -> str
    """
    return (arrow.get(date_time, format).shift(
        years=year,
        months=month,
        days=day,
        hours=hour,
        minutes=minute,
        seconds=second,
    ).format(format))


def conduct_shift(shift: str):
    year = 0
    month = 0
    day = 0
    hour = 0
    minute = 0
    second = 0
    shift_list = ["Y", "M", "D", "H", "m", "s"]
    # 不包含shift中字符 默认为日
    if shift[-1] not in shift_list:
        day = int(shift)
    else:
        if shift[-1] == "Y":
            year = int(shift[:-1])
        if shift[-1] == "M":
            month = int(shift[:-1])
        if shift[-1] == "D":
            day = int(shift[:-1])
        if shift[-1] == "H":
            hour = int(shift[:-1])
        if shift[-1] == "m":
            minute = int(shift[:-1])
        if shift[-1] == "s":
            second = int(shift[:-1])

    return {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second,
    }


def conduct_add_subtract_shift(shifts):
    shift = {
        "year": 0,
        "month": 0,
        "day": 0,
        "hour": 0,
        "minute": 0,
        "second": 0
    }
    if "+" in shifts or "-" in shifts:
        begin = shifts.split("+")[0] if "+" in shifts else shifts.split("-")[0]
        end = shifts.replace(begin, "", 1)
        begin_shift: Dict[str, int] = conduct_shift(begin)
        end_shift: Dict[str, int] = conduct_shift(end)
        shift["year"] = begin_shift.get("year") + end_shift.get("year")
        shift["month"] = begin_shift.get("month") + end_shift.get("month")
        shift["day"] = begin_shift.get("day") + end_shift.get("day")
        shift["hour"] = begin_shift.get("hour") + end_shift.get("hour")
        shift["minute"] = begin_shift.get("minute") + end_shift.get("minute")
        shift["second"] = begin_shift.get("second") + end_shift.get("second")
    else:
        shift = conduct_shift(shifts)
    return shift


def get_last_any_day(last_day: int = 1):
    return get_any_datetime(date_time=get_current_date(),
                            day=-last_day,
                            format="YYYY-MM-DD")


def cal_date(date1, date2):
    """
    计算日期差
    :param date1:   开始日期
    :param date2:   结束日期
    """
    date1 = time.strptime(date1, "%Y-%m-%d")
    date2 = time.strptime(date2, "%Y-%m-%d")
    date1 = datetime.datetime(date1[0], date1[1], date1[2])
    date2 = datetime.datetime(date2[0], date2[1], date2[2])
    cal = date2 - date1
    return cal.days

