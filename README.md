## 数据提取
```python

from humo_utils import analytic

if __name__ == '__main__':
    data_json = {
        "id": "3f2f22e6aad9433aa706a3a187e1dfa6",
        "create_time": "2022-04-20 22:53:51",
        "update_time": "2022-04-24 18:00:07",
        "username": "mini_right",
        "nickname": "小右",
        "mobile": "13800000000",
        "email": "www@anyu.wang",
        "status": 1
    }
    data_xml = """
        <body>
            <id>3f2f22e6aad9433aa706a3a187e1dfa6</id>
            <create_time>2022-04-20 22:53:51</create_time>
            <update_time>2022-04-24 18:00:07</update_time>
            <username>mini_right</username>
            <nickname>小右</nickname>
            <mobile>13800000000</mobile>
            <email>www@anyu.wang</email>
            <status>1</status>
        </body>
    """

    print(analytic(data_json, 'nickname'))
    print(analytic(data_xml, 'nickname'))

```

## 数据转换

### Excel

```python

from humo_utils import ToExcel

if __name__ == '__main__':
    excel_path = '/Users/mini-right/Desktop/test.xls'
    data = [
        {
            "id": "3f2f22e6aad9433aa706a3a187e1dfa6",
            "create_time": "2022-04-20 22:53:51",
            "update_time": "2022-04-24 18:00:07",
            "username": "mini_right",
            "nickname": "小右",
            "mobile": "13800000000",
            "email": "www@anyu.wang",
            "status": 1
        }
    ]

    excel = ToExcel(excel_path)
    excel.sheet(
        title=list(data[0].keys()),
        table_data=data,
        sheet_name='第一个sheet页'
    )
    excel.close()
```

### PDF转图片
```python
from humo_utils import pdf2img

if __name__ == '__main__':
    pdf2img(
        pdf_path='/Users/mini-right/Documents/第一个PDF.PDF',
        save_path='/Users/mini-right/Documents',
        img_name='第一个PDF',
        page_list=[1, 3]
    )
```

## 日期处理
```python

from humo_utils import (get_current_millisecond_time,
                        get_current_second_time,
                        get_current_date,
                        get_current_time,
                        get_current_datetime,
                        get_current_week_day,
                        get_last_week_start_date,
                        get_last_week_end_date,
                        get_birthday_date,
                        get_any_datetime,
                        get_last_any_day,
                        cal_date)

if __name__ == '__main__':
    # 获取当前时间戳-毫秒级
    print(get_current_millisecond_time())

    # 获取当前时间戳 - 秒级
    print(get_current_second_time())

    # 获取当前日期
    print(get_current_date())

    # 获取当前时间
    print(get_current_time())

    # 获取当前日期时间
    print(get_current_datetime())

    # 获取当前是周几
    print(get_current_week_day())

    # 获取上周一日期
    print(get_last_week_start_date())

    # 获取上周末日期
    print(get_last_week_end_date())

    # 根据年龄获取出生日期
    # 支持年龄类型: 18Y 18Y-1D 18Y+1M
    # Y年 M月 D日
    # 以date_time参数为基准进行计算
    print(get_birthday_date('1Y-1D', '2020-01-01'))

    # 获取距离传入日期的任意偏移时间的日期时间
    # 默认为当前日期时间  格式为YYYY-MM-DD HH:mm:ss (date_time要与format格式相同)
    print(get_any_datetime(
        date_time='2022-01-01 00:00:00',
        year=1
    ))
    print(get_any_datetime(
        date_time='2022-01-01',
        year=1,
        format='YYYY-MM-DD'
    ))

    # 获取最近日期
    print(get_last_any_day())

    # 计算日期差
    # 以date2为基准计算与date1的时间差
    print(cal_date('2022-01-02', '2022-01-01'))

```

## 文件下载
```python
from humo_utils import Down

if __name__ == '__main__':
    Down.main(
        url='https://cdn.nlark.com/yuque/0/2021/jpeg/anonymous/1637675879100-f1281f5d-060a-48ce-b674-3245e4ea093e.jpeg?x-oss-process=image%2Fresize%2Cm_fill%2Cw_320%2Ch_320%2Fformat%2Cpng',
        local_path='/Users/mini-right/Desktop/poloyy.png',
        refresh=True,
        progress=True
    )

```

## 生成器

```python

from humo_utils import generate_card, generate_name, generate_mobile, generate_address, generate_identity_info

if __name__ == '__main__':
    # 生成指定出生日期身份证号
    print(generate_card(
        birthday='2000-01-01',
        sex='1'
    ))
    # 生成指定年龄身份证号
    print(generate_card(
        age='18Y',
        sex='2',
        address='110101'
    ))

    # 生成姓名
    print(generate_name())

    # 生成手机号
    print(generate_mobile())

    # 生成地址
    print(generate_address(address_no='110101'))

    # 生成完整身份信息
    print(generate_identity_info(age='10Y', sex='2'))

```

## 文件夹压缩
```python
from humo_utils import write_all_file_to_zip

if __name__ == '__main__':
    write_all_file_to_zip(
        dir_path='/Users/mini-right/Desktop/未命名文件夹',
        zip_path='/Users/mini-right/Desktop/未命名文件夹.zip'
    )
```